#!/usr/bin/env python3
"""
Git Dirty CLI - Command-line interface for scanning dirty Git repositories.

Usage:
    git-dirty [PATH] [OPTIONS]
    dirty-git [PATH] [OPTIONS]
"""

__version__ = "2.2.0"

import argparse
import json
import os
import subprocess
import sys
from typing import Dict, List, Optional


class RepoScanner:
    """Scans directories for Git repositories and checks their status."""

    def __init__(self):
        self.excluded_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', '.tox', '.eggs'}

    def scan(self, root_path: str, max_depth: int = 10,
             progress_callback=None) -> List[Dict]:
        """Scan directory tree for Git repositories."""
        repositories = []
        self._scan_recursive(root_path, repositories, 0, max_depth, progress_callback)
        return repositories

    def _scan_recursive(self, current_path: str, repositories: List[Dict],
                        depth: int, max_depth: int, progress_callback) -> None:
        """Recursively scan directories."""
        if depth > max_depth:
            return

        try:
            if not os.path.isdir(current_path):
                return

            if progress_callback:
                progress_callback(current_path)

            # Check if this is a git repo
            if os.path.exists(os.path.join(current_path, '.git')):
                repo_info = self._get_repo_info(current_path)
                repositories.append(repo_info)
                return  # Don't scan inside git repos

            # Scan subdirectories
            try:
                entries = os.listdir(current_path)
            except PermissionError:
                return

            for entry in sorted(entries):
                if entry.startswith('.') and entry != '.git':
                    continue
                if entry in self.excluded_dirs:
                    continue

                entry_path = os.path.join(current_path, entry)
                if os.path.isdir(entry_path):
                    self._scan_recursive(entry_path, repositories, depth + 1,
                                        max_depth, progress_callback)
        except (OSError, PermissionError):
            pass

    def _get_repo_info(self, repo_path: str) -> Dict:
        """Get detailed information about a Git repository."""
        info = {
            'path': repo_path,
            'name': os.path.basename(repo_path),
            'branch': 'unknown',
            'has_uncommitted': False,
            'has_remote': False,
            'has_unpushed': False,
            'changes': [],
            'changes_count': 0,
        }

        try:
            # Get branch
            result = subprocess.run(
                ['git', 'branch', '--show-current'],
                cwd=repo_path, capture_output=True, text=True, timeout=5
            )
            info['branch'] = result.stdout.strip() or 'detached HEAD'

            # Get status
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                cwd=repo_path, capture_output=True, text=True, timeout=10
            )
            status_lines = [l for l in result.stdout.strip().split('\n') if l.strip()]
            info['has_uncommitted'] = bool(status_lines)
            info['changes'] = status_lines[:5]
            info['changes_count'] = len(status_lines)

            # Check remote
            result = subprocess.run(
                ['git', 'remote'],
                cwd=repo_path, capture_output=True, text=True, timeout=5
            )
            info['has_remote'] = bool(result.stdout.strip())

            # Check unpushed commits
            if info['has_remote']:
                result = subprocess.run(
                    ['git', 'rev-parse', '--abbrev-ref', '--symbolic-full-name', '@{u}'],
                    cwd=repo_path, capture_output=True, text=True, timeout=5
                )
                if result.returncode == 0:
                    result = subprocess.run(
                        ['git', 'rev-list', '--count', '@{u}..HEAD'],
                        cwd=repo_path, capture_output=True, text=True, timeout=5
                    )
                    if result.returncode == 0:
                        try:
                            info['has_unpushed'] = int(result.stdout.strip()) > 0
                        except ValueError:
                            pass
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
            pass

        return info


def is_dirty(repo: Dict, check_uncommitted: bool, check_no_remote: bool,
             check_unpushed: bool) -> bool:
    """Determine if a repository is considered dirty based on criteria."""
    if check_uncommitted and repo.get('has_uncommitted', False):
        return True
    if check_no_remote and not repo.get('has_remote', True):
        return True
    if check_unpushed and repo.get('has_unpushed', False):
        return True
    return False


def format_changes(repo: Dict) -> str:
    """Format changes summary."""
    if not repo.get('has_uncommitted'):
        return '-'

    changes = repo.get('changes', [])
    counts = {'M': 0, 'A': 0, 'D': 0, '?': 0, 'R': 0}

    for line in changes:
        if len(line) >= 2:
            for char in line[:2]:
                if char in counts:
                    counts[char] += 1

    parts = []
    if counts['M']: parts.append(f"{counts['M']}M")
    if counts['A']: parts.append(f"{counts['A']}A")
    if counts['D']: parts.append(f"{counts['D']}D")
    if counts['?']: parts.append(f"{counts['?']}?")
    if counts['R']: parts.append(f"{counts['R']}R")

    total = repo.get('changes_count', 0)
    if total > 5:
        parts.append(f"+{total - 5}")

    return ' '.join(parts) if parts else '-'


def print_table(repos: List[Dict], use_color: bool,
                check_uncommitted: bool, check_no_remote: bool,
                check_unpushed: bool) -> None:
    """Print repositories in table format."""
    if not repos:
        print("No repositories found.")
        return

    # Color codes
    RED = '\033[91m' if use_color else ''
    GREEN = '\033[92m' if use_color else ''
    YELLOW = '\033[93m' if use_color else ''
    RESET = '\033[0m' if use_color else ''
    BOLD = '\033[1m' if use_color else ''

    # Calculate column widths
    name_width = min(25, max(len(r['name']) for r in repos))
    branch_width = min(15, max(len(r['branch']) for r in repos))

    # Header
    header = f"{'Repository':<{name_width}}  {'Branch':<{branch_width}}  {'Status':<7}  {'Changes':<12}  {'Remote':<8}  {'Unpushed':<8}"
    print(f"\n{BOLD}{header}{RESET}")
    print("-" * len(header))

    # Rows
    for repo in repos:
        dirty = is_dirty(repo, check_uncommitted, check_no_remote, check_unpushed)

        name = repo['name'][:name_width]
        branch = repo['branch'][:branch_width]
        status = f"{RED}DIRTY{RESET}" if dirty else f"{GREEN}clean{RESET}"
        changes = format_changes(repo)
        remote = f"{YELLOW}no{RESET}" if not repo['has_remote'] else 'yes'
        unpushed = f"{YELLOW}yes{RESET}" if repo['has_unpushed'] else '-'

        print(f"{name:<{name_width}}  {branch:<{branch_width}}  {status:<7}  {changes:<12}  {remote:<8}  {unpushed:<8}")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog='git-dirty',
        description='Scan for Git repositories with uncommitted changes',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  git-dirty                    Scan current directory
  dirty-git ~/projects         Scan specific path
  git-dirty --dirty-only       Show only dirty repos
  git-dirty --json             Output as JSON
  git-dirty -q                 Quiet mode (paths only)
'''
    )

    parser.add_argument('path', nargs='?', default='.',
                        help='Path to scan (default: current directory)')
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')

    # Filter options
    filter_group = parser.add_argument_group('filter options')
    filter_group.add_argument('--dirty-only', '-d', action='store_true',
                              help='Show only dirty repositories')
    filter_group.add_argument('--clean-only', '-c', action='store_true',
                              help='Show only clean repositories')

    # Dirty criteria
    criteria_group = parser.add_argument_group('dirty criteria (default: --uncommitted --no-remote)')
    criteria_group.add_argument('--uncommitted', '-u', action='store_true',
                                help='Consider uncommitted changes as dirty')
    criteria_group.add_argument('--no-remote', '-r', action='store_true',
                                help='Consider missing remote as dirty')
    criteria_group.add_argument('--unpushed', '-p', action='store_true',
                                help='Consider unpushed commits as dirty')
    criteria_group.add_argument('--all-criteria', '-a', action='store_true',
                                help='Enable all dirty criteria')

    # Output options
    output_group = parser.add_argument_group('output options')
    output_group.add_argument('--json', '-j', action='store_true',
                              help='Output as JSON')
    output_group.add_argument('--quiet', '-q', action='store_true',
                              help='Quiet mode: only print paths')
    output_group.add_argument('--no-color', action='store_true',
                              help='Disable colored output')

    # Scan options
    scan_group = parser.add_argument_group('scan options')
    scan_group.add_argument('--max-depth', '-m', type=int, default=10,
                            help='Maximum scan depth (default: 10)')
    scan_group.add_argument('--no-progress', action='store_true',
                            help='Disable progress output')

    args = parser.parse_args()

    # Resolve path
    scan_path = os.path.abspath(os.path.expanduser(args.path))
    if not os.path.isdir(scan_path):
        print(f"Error: '{scan_path}' is not a valid directory", file=sys.stderr)
        sys.exit(1)

    # Set default criteria if none specified
    check_uncommitted = args.uncommitted or args.all_criteria
    check_no_remote = args.no_remote or args.all_criteria
    check_unpushed = args.unpushed or args.all_criteria

    # Default: uncommitted + no-remote
    if not (args.uncommitted or args.no_remote or args.unpushed or args.all_criteria):
        check_uncommitted = True
        check_no_remote = True

    # Determine color usage
    use_color = not args.no_color and sys.stdout.isatty() and not args.json and not args.quiet

    # Progress callback
    last_dir = [None]
    def progress_callback(current_dir):
        if not args.no_progress and not args.quiet and not args.json:
            # Clear line and print current directory
            short_dir = current_dir
            if len(short_dir) > 60:
                short_dir = '...' + short_dir[-57:]
            print(f"\rScanning: {short_dir:<60}", end='', flush=True)
            last_dir[0] = current_dir

    # Scan
    scanner = RepoScanner()
    repos = scanner.scan(scan_path, args.max_depth, progress_callback)

    # Clear progress line
    if not args.no_progress and not args.quiet and not args.json:
        print("\r" + " " * 70 + "\r", end='')

    # Filter by dirty status
    for repo in repos:
        repo['is_dirty'] = is_dirty(repo, check_uncommitted, check_no_remote, check_unpushed)

    if args.dirty_only:
        repos = [r for r in repos if r['is_dirty']]
    elif args.clean_only:
        repos = [r for r in repos if not r['is_dirty']]

    # Output
    if args.json:
        print(json.dumps(repos, indent=2))
    elif args.quiet:
        for repo in repos:
            print(repo['path'])
    else:
        dirty_count = sum(1 for r in repos if r['is_dirty'])
        total = len(repos)

        if use_color:
            print(f"Found {total} repositories, \033[91m{dirty_count} dirty\033[0m")
        else:
            print(f"Found {total} repositories, {dirty_count} dirty")

        print_table(repos, use_color, check_uncommitted, check_no_remote, check_unpushed)

    # Exit code: 1 if dirty repos found (useful for scripting)
    if args.dirty_only or args.clean_only:
        sys.exit(0 if repos else 1)
    else:
        sys.exit(1 if any(r['is_dirty'] for r in repos) else 0)


if __name__ == '__main__':
    main()
