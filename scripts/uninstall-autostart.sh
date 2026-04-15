#!/bin/bash
# Uninstallation script for Dirty Git Finder
# This script removes the autostart and application menu entries

echo "===================================="
echo "  Dirty Git Finder - Deinstallation"
echo "===================================="
echo ""

# Remove from autostart
AUTOSTART_FILE="$HOME/.config/autostart/dirty-git-finder.desktop"
if [ -f "$AUTOSTART_FILE" ]; then
    rm "$AUTOSTART_FILE"
    echo "✓ Autostart-Eintrag entfernt"
else
    echo "- Autostart-Eintrag nicht vorhanden"
fi

# Remove from applications menu
APPS_FILE="$HOME/.local/share/applications/dirty-git-finder.desktop"
if [ -f "$APPS_FILE" ]; then
    rm "$APPS_FILE"
    echo "✓ Anwendungsmenü-Eintrag entfernt"
else
    echo "- Anwendungsmenü-Eintrag nicht vorhanden"
fi

# Remove symlink from ~/.local/bin
SYMLINK="$HOME/.local/bin/dirty-git-finder"
if [ -L "$SYMLINK" ] || [ -e "$SYMLINK" ]; then
    rm "$SYMLINK"
    echo "✓ CLI-Symlink entfernt"
else
    echo "- CLI-Symlink nicht vorhanden"
fi

echo ""
echo "===================================="
echo "  Deinstallation abgeschlossen!"
echo "===================================="
echo ""
echo "Hinweis: Die Anwendungsdateien sind noch im Projektverzeichnis vorhanden."
echo "Zum manuellen Starten: python3 dirty_git_finder.py"
echo ""
