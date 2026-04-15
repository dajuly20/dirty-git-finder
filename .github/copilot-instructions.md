# Dirty Git Repository Finder GUI

This project is a Python GUI application that scans the user's system for Git repositories and identifies which ones have uncommitted changes (are "dirty").

## Project Structure

```
scan-for-dirty-git-repos-gui/
├── dirty_git_finder.py         # Main GUI application with integrated scanner
├── git_scanner.py              # Standalone scanner module for CLI usage
├── run.py                      # Launcher script
├── launch.sh                   # Shell launcher for autostart
├── autostart-install.sh        # Installation script (prompts for autostart)
├── uninstall-autostart.sh      # Uninstallation script
├── dirty-git-finder.desktop    # Desktop entry template
├── README.md                   # User documentation
├── AUTOSTART-GUIDE.md          # Detailed autostart guide
└── .github/
    └── copilot-instructions.md # This file
```

## Key Components

- **dirty_git_finder.py**: Main application with tkinter GUI and built-in `GitRepoScanner` class
- **git_scanner.py**: Separate, reusable scanner module with `GitScanner` and `GitRepository` classes for CLI usage

## Development Guidelines

- Use Python 3.7+ with tkinter for cross-platform compatibility
- Implement proper error handling for git operations
- Provide clear visual feedback during scanning operations
- Display results in an organized, filterable format
- Use threading for background scanning to keep UI responsive
- Support Linux, macOS, and Windows platforms

## Autostart Implementation

- Linux: XDG autostart via `~/.config/autostart/*.desktop`
- macOS: LaunchAgent via `~/Library/LaunchAgents/*.plist`
- Windows: Registry entry in `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`

## Code Style

- Use descriptive variable and function names
- Add docstrings to classes and public methods
- Handle exceptions gracefully with user-friendly error messages
- Use `os.path.realpath()` for symlink resolution
- Generate paths dynamically, never hardcode absolute paths
