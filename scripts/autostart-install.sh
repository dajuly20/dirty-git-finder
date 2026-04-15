#!/bin/bash
# Installation script for Dirty Git Finder
# This script sets up the application and optionally enables autostart

set -e

echo "=================================="
echo "  Dirty Git Finder - Installation"
echo "=================================="
echo ""

# Get the directory where this script is located (scripts/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Get the project root (one level up from scripts/)
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Create ~/.local/bin if it doesn't exist
BIN_DIR="$HOME/.local/bin"
mkdir -p "$BIN_DIR"

# Make the launcher script executable
chmod +x "$SCRIPT_DIR/launch.sh"
chmod +x "$PROJECT_ROOT/run.py"
chmod +x "$PROJECT_ROOT/src/dirty_git_finder.py"

echo "✓ Scripts ausführbar gemacht"

# Create symlink in ~/.local/bin
SYMLINK_NAME="dirty-git-finder"
if [ -L "$BIN_DIR/$SYMLINK_NAME" ] || [ -e "$BIN_DIR/$SYMLINK_NAME" ]; then
    rm "$BIN_DIR/$SYMLINK_NAME"
fi
ln -s "$SCRIPT_DIR/launch.sh" "$BIN_DIR/$SYMLINK_NAME"
echo "✓ CLI-Symlink erstellt: $BIN_DIR/$SYMLINK_NAME"

# Check if ~/.local/bin is in PATH
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo ""
    echo "⚠️  HINWEIS: $BIN_DIR ist nicht in deinem PATH!"
    echo "   Füge folgende Zeile zu ~/.bashrc oder ~/.zshrc hinzu:"
    echo "   export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo ""
fi

# Generate desktop entry content
generate_desktop_entry() {
    cat << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Dirty Git Finder
GenericName=Git Repository Monitor
Comment=Scans for Git repositories and shows which ones have uncommitted changes
Exec=$BIN_DIR/$SYMLINK_NAME
Path=$PROJECT_ROOT
Icon=git
Terminal=false
Categories=Development;Utility;
StartupNotify=false
X-GNOME-Autostart-enabled=true
EOF
}

# Install to applications directory for the application menu
APPS_DIR="$HOME/.local/share/applications"
mkdir -p "$APPS_DIR"
generate_desktop_entry > "$APPS_DIR/dirty-git-finder.desktop"
echo "✓ Anwendungsmenü-Eintrag erstellt: $APPS_DIR/dirty-git-finder.desktop"

# Create log directory (optional, for debugging)
LOG_DIR="$HOME/.local/share/dirty-git-finder"
mkdir -p "$LOG_DIR"

# Ask about autostart
echo ""
echo "=================================="
read -p "Soll Dirty Git Finder beim Systemstart automatisch starten? (j/n): " ENABLE_AUTOSTART

AUTOSTART_DIR="$HOME/.config/autostart"

if [[ "$ENABLE_AUTOSTART" =~ ^[jJyY]$ ]]; then
    mkdir -p "$AUTOSTART_DIR"
    generate_desktop_entry > "$AUTOSTART_DIR/dirty-git-finder.desktop"
    echo "✓ Autostart aktiviert: $AUTOSTART_DIR/dirty-git-finder.desktop"
else
    # Remove autostart entry if it exists
    if [ -f "$AUTOSTART_DIR/dirty-git-finder.desktop" ]; then
        rm "$AUTOSTART_DIR/dirty-git-finder.desktop"
        echo "✓ Autostart deaktiviert"
    else
        echo "✓ Autostart bleibt deaktiviert"
    fi
fi

echo ""
echo "=================================="
echo "  Installation abgeschlossen!"
echo "=================================="
echo ""
echo "Starten mit:"
echo "  dirty-git-finder"
echo ""
echo "Deinstallieren mit:"
echo "  $SCRIPT_DIR/uninstall-autostart.sh"
echo ""
