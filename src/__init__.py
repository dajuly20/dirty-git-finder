"""
Dirty Git Finder - A GUI application to scan for Git repositories with uncommitted changes.
"""

from .dirty_git_finder import main, DirtyGitFinderGUI, GitRepoScanner, __version__

__all__ = ['main', 'DirtyGitFinderGUI', 'GitRepoScanner', '__version__']
