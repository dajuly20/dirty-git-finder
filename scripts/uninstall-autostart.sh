#!/bin/bash
# Uninstallation script for Dirty Git Finder autostart
# This script removes the autostart configuration

echo "Uninstalling Dirty Git Finder Autostart..."

# Remove from autostart
AUTOSTART_FILE="$HOME/.config/autostart/dirty-git-finder.desktop"
if [ -f "$AUTOSTART_FILE" ]; then
    rm "$AUTOSTART_FILE"
    echo "Removed autostart entry: $AUTOSTART_FILE"
else
    echo "Autostart entry not found (already removed)"
fi

# Remove from applications menu
APPS_FILE="$HOME/.local/share/applications/dirty-git-finder.desktop"
if [ -f "$APPS_FILE" ]; then
    rm "$APPS_FILE"
    echo "Removed application menu entry: $APPS_FILE"
else
    echo "Application menu entry not found (already removed)"
fi

# Remove symlink from ~/.local/bin
SYMLINK="$HOME/.local/bin/dirty-git-finder"
if [ -L "$SYMLINK" ] || [ -e "$SYMLINK" ]; then
    rm "$SYMLINK"
    echo "Removed symlink: $SYMLINK"
else
    echo "Symlink not found (already removed)"
fi

echo ""
echo "Uninstallation complete!"
echo "The Dirty Git Finder will no longer start automatically."
echo ""
echo "Note: The application files are still in the project directory."
echo "To start manually, run: python3 run.py"
