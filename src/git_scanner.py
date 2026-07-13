"""
Git Repository Scanner Module
Provides functionality to scan directories for Git repositories and check their status.

This is a standalone module that can be used independently of the GUI application.
For GUI usage, see dirty_git_finder.py which has its own integrated scanner.
"""

__version__ = "2.2.1"

import os
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Callable


class GitRepository:
    """Represents a Git repository with status information."""
    
    def __init__(self, path: str):
        self.path = path
        self.name = os.path.basename(path)
        self._status_cache = None
    
    @property
    def is_git_repo(self) -> bool:
        """Check if the path is a valid Git repository."""
        return os.path.exists(os.path.join(self.path, '.git'))
    
    def get_status(self, force_refresh: bool = False) -> Dict:
        """Get the current status of the Git repository."""
        if self._status_cache is None or force_refresh:
            self._status_cache = self._fetch_status()
        return self._status_cache
    
    def _fetch_status(self) -> Dict:
        """Fetch status information from Git."""
        try:
            # Get current branch
            branch_result = subprocess.run(
                ['git', 'branch', '--show-current'],
                cwd=self.path,
                capture_output=True,
                text=True,
                timeout=5
            )
            current_branch = branch_result.stdout.strip() or "detached HEAD"
            
            # Get porcelain status
            status_result = subprocess.run(
                ['git', 'status', '--porcelain'],
                cwd=self.path,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            status_lines = [line for line in status_result.stdout.strip().split('\n') if line.strip()]
            
            # Analyze changes
            changes = self._analyze_changes(status_lines)
            
            return {
                'branch': current_branch,
                'is_dirty': bool(status_lines),
                'total_changes': len(status_lines),
                'changes': changes,
                'status_lines': status_lines[:10]  # Limit to first 10 for display
            }
            
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError) as e:
            return {
                'branch': 'unknown',
                'is_dirty': False,
                'total_changes': 0,
                'changes': {'modified': 0, 'added': 0, 'deleted': 0, 'untracked': 0},
                'status_lines': [],
                'error': str(e)
            }
    
    def _analyze_changes(self, status_lines: List[str]) -> Dict[str, int]:
        """Analyze Git status lines to categorize changes."""
        changes = {'modified': 0, 'added': 0, 'deleted': 0, 'untracked': 0, 'renamed': 0}
        
        for line in status_lines:
            if len(line) < 2:
                continue
                
            index_status = line[0]
            worktree_status = line[1]
            
            # Check index status
            if index_status == 'A':
                changes['added'] += 1
            elif index_status == 'M':
                changes['modified'] += 1
            elif index_status == 'D':
                changes['deleted'] += 1
            elif index_status == 'R':
                changes['renamed'] += 1
            
            # Check worktree status
            if worktree_status == 'M':
                changes['modified'] += 1
            elif worktree_status == 'D':
                changes['deleted'] += 1
            elif worktree_status == '?':
                changes['untracked'] += 1
        
        return changes


class GitScanner:
    """Scans directories for Git repositories."""
    
    def __init__(self):
        self.cancel_requested = False
        self.excluded_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}
    
    def scan(
        self,
        root_path: str,
        progress_callback: Optional[Callable[[str], None]] = None,
        repo_found_callback: Optional[Callable[[GitRepository], None]] = None,
        max_depth: int = 10
    ) -> List[GitRepository]:
        """
        Scan a directory tree for Git repositories.
        
        Args:
            root_path: Root directory to start scanning
            progress_callback: Called with current directory being scanned
            repo_found_callback: Called when a Git repository is found
            max_depth: Maximum depth to scan (prevents infinite recursion)
        
        Returns:
            List of GitRepository objects found
        """
        repositories = []
        self.cancel_requested = False
        
        try:
            repositories = self._scan_recursive(
                root_path, 
                repositories, 
                progress_callback, 
                repo_found_callback,
                current_depth=0,
                max_depth=max_depth
            )
        except KeyboardInterrupt:
            pass  # Graceful cancellation
        
        return repositories
    
    def _scan_recursive(
        self,
        current_path: str,
        repositories: List[GitRepository],
        progress_callback: Optional[Callable[[str], None]],
        repo_found_callback: Optional[Callable[[GitRepository], None]],
        current_depth: int,
        max_depth: int
    ) -> List[GitRepository]:
        """Recursively scan directories for Git repositories."""
        
        if self.cancel_requested or current_depth > max_depth:
            return repositories
        
        try:
            if not os.path.exists(current_path) or not os.path.isdir(current_path):
                return repositories
            
            # Update progress
            if progress_callback:
                progress_callback(current_path)
            
            # Check if current directory is a Git repository
            if self._is_git_repository(current_path):
                repo = GitRepository(current_path)
                repositories.append(repo)
                
                if repo_found_callback:
                    repo_found_callback(repo)
                
                # Don't scan inside Git repositories
                return repositories
            
            # Scan subdirectories
            try:
                entries = os.listdir(current_path)
            except PermissionError:
                return repositories  # Skip directories we can't read
            
            for entry in entries:
                if self.cancel_requested:
                    break
                
                if entry.startswith('.') and entry not in {'.git'}:
                    continue  # Skip most hidden directories
                
                if entry in self.excluded_dirs:
                    continue
                
                entry_path = os.path.join(current_path, entry)
                
                if os.path.isdir(entry_path):
                    self._scan_recursive(
                        entry_path,
                        repositories,
                        progress_callback,
                        repo_found_callback,
                        current_depth + 1,
                        max_depth
                    )
            
        except (OSError, PermissionError):
            pass  # Skip problematic directories
        
        return repositories
    
    def _is_git_repository(self, path: str) -> bool:
        """Check if a directory contains a Git repository."""
        git_dir = os.path.join(path, '.git')
        return os.path.exists(git_dir) and (
            os.path.isdir(git_dir) or 
            (os.path.isfile(git_dir) and self._is_git_worktree(git_dir))
        )
    
    def _is_git_worktree(self, git_file_path: str) -> bool:
        """Check if .git file points to a Git worktree."""
        try:
            with open(git_file_path, 'r') as f:
                content = f.read().strip()
                return content.startswith('gitdir:')
        except (OSError, IOError):
            return False
    
    def cancel(self):
        """Cancel the current scan operation."""
        self.cancel_requested = True
    
    def add_excluded_dir(self, dirname: str):
        """Add a directory name to the exclusion list."""
        self.excluded_dirs.add(dirname)
    
    def remove_excluded_dir(self, dirname: str):
        """Remove a directory name from the exclusion list."""
        self.excluded_dirs.discard(dirname)