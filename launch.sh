#!/bin/bash
# Launcher script for Dirty Git Finder GUI
# This script ensures the application runs from the correct directory

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the script directory
cd "$SCRIPT_DIR"

# Launch the application (detached from terminal)
nohup python3 "$SCRIPT_DIR/run.py" > /dev/null 2>&1 &

# Optional: Log startup for debugging
# mkdir -p "$HOME/.local/share/dirty-git-finder"
# echo "$(date): Dirty Git Finder started" >> "$HOME/.local/share/dirty-git-finder/startup.log"
