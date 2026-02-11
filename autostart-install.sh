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

# Create ~/.local/bin if it doesn't exist
BIN_DIR="$HOME/.local/bin"
mkdir -p "$BIN_DIR"

# Make the launcher script executable
chmod +x "$SCRIPT_DIR/launch.sh"
chmod +x "$SCRIPT_DIR/run.py"
chmod +x "$SCRIPT_DIR/dirty_git_finder.py"

echo "Made scripts executable"

# Create symlink in ~/.local/bin
SYMLINK_NAME="dirty-git-finder"
if [ -L "$BIN_DIR/$SYMLINK_NAME" ] || [ -e "$BIN_DIR/$SYMLINK_NAME" ]; then
    rm "$BIN_DIR/$SYMLINK_NAME"
fi
ln -s "$SCRIPT_DIR/launch.sh" "$BIN_DIR/$SYMLINK_NAME"
echo "Created symlink: $BIN_DIR/$SYMLINK_NAME -> $SCRIPT_DIR/launch.sh"

# Check if ~/.local/bin is in PATH
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo ""
    echo "⚠️  HINWEIS: $BIN_DIR ist nicht in deinem PATH!"
    echo "   Füge folgende Zeile zu ~/.bashrc oder ~/.zshrc hinzu:"
    echo "   export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo ""
fi

# Generate desktop file with correct paths (don't use static file with hardcoded paths)
DESKTOP_FILE="$AUTOSTART_DIR/dirty-git-finder.desktop"
cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Dirty Git Finder
GenericName=Git Repository Monitor
Comment=Scans for Git repositories and shows which ones have uncommitted changes
Exec=$BIN_DIR/$SYMLINK_NAME
Path=$SCRIPT_DIR
Icon=git
Terminal=false
Categories=Development;Utility;
StartupNotify=false
X-GNOME-Autostart-enabled=true
EOF

chmod +x "$DESKTOP_FILE"
echo "Installed autostart entry to: $DESKTOP_FILE"

# Also copy to applications directory for the application menu (optional)
APPS_DIR="$HOME/.local/share/applications"
mkdir -p "$APPS_DIR"
cp "$DESKTOP_FILE" "$APPS_DIR/"
chmod +x "$APPS_DIR/dirty-git-finder.desktop"

echo "Installed application menu entry to: $APPS_DIR/dirty-git-finder.desktop"

# Create log directory (optional, for debugging)
LOG_DIR="$HOME/.local/share/dirty-git-finder"
mkdir -p "$LOG_DIR"

echo ""
echo "Installation complete!"
echo ""
echo "The Dirty Git Finder will now start automatically when you log in."
echo ""
echo "To start manually, run:"
echo "  dirty-git-finder"
echo ""
echo "To uninstall, run:"
echo "  $SCRIPT_DIR/uninstall-autostart.sh"
