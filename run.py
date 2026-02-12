#!/usr/bin/env python3
"""
Simple launcher script for the Dirty Git Finder GUI application.
This provides an easy way to start the application.
"""

import sys
import os

# Add the src directory to the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(script_dir, 'src'))

try:
    from dirty_git_finder import main
    
    if __name__ == "__main__":
        main()
        
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Please ensure all required files are present and Python dependencies are installed.")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)