#!/bin/bash
# Installation script for Dirty Git Finder autostart
# This script sets up the application to run automatically at login

set -e

echo "Installing Dirty Git Finder Autostart..."

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create autostart directory if it doesn't exist
AUTOSTART_DIR="$HOME/.config/autostart"
mkdir -p "$AUTOSTART_DIR"

# Make the launcher script executable
chmod +x "$SCRIPT_DIR/launch.sh"
chmod +x "$SCRIPT_DIR/run.py"
chmod +x "$SCRIPT_DIR/dirty_git_finder.py"

echo "Made scripts executable"

# Copy the desktop file to autostart directory
cp "$SCRIPT_DIR/dirty-git-finder.desktop" "$AUTOSTART_DIR/"

echo "Installed autostart entry to: $AUTOSTART_DIR/dirty-git-finder.desktop"

# Also copy to applications directory for the application menu (optional)
APPS_DIR="$HOME/.local/share/applications"
mkdir -p "$APPS_DIR"
cp "$SCRIPT_DIR/dirty-git-finder.desktop" "$APPS_DIR/"

echo "Installed application menu entry to: $APPS_DIR/dirty-git-finder.desktop"

# Create log directory (optional, for debugging)
LOG_DIR="$HOME/.local/share/dirty-git-finder"
mkdir -p "$LOG_DIR"

echo ""
echo "Installation complete!"
echo ""
echo "The Dirty Git Finder will now start automatically when you log in."
echo ""
echo "To manage autostart:"
echo "  - Enable:  cp '$SCRIPT_DIR/dirty-git-finder.desktop' '$AUTOSTART_DIR/'"
echo "  - Disable: rm '$AUTOSTART_DIR/dirty-git-finder.desktop'"
echo ""
echo "To start manually right now:"
echo "  $SCRIPT_DIR/launch.sh"
echo ""
echo "To uninstall:"
echo "  rm '$AUTOSTART_DIR/dirty-git-finder.desktop'"
echo "  rm '$APPS_DIR/dirty-git-finder.desktop'"
