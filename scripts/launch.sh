#!/bin/bash
# Launcher script for Dirty Git Finder GUI
# This script ensures the application runs from the correct directory

# Get the directory where the actual script is located (follow symlinks)
SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"

# Get the project root (one level up from scripts/)
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Change to the project root directory
cd "$PROJECT_ROOT"

# Launch the application (detached from terminal)
nohup python3 "$PROJECT_ROOT/run.py" > /dev/null 2>&1 &

# Optional: Log startup for debugging
# mkdir -p "$HOME/.local/share/dirty-git-finder"
# echo "$(date): Dirty Git Finder started" >> "$HOME/.local/share/dirty-git-finder/startup.log"
