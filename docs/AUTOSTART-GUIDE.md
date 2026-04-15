# Autostart Setup Guide

This guide explains how to set up the Dirty Git Finder to start automatically when you log in to your Linux system.

## Quick Start

### Install Autostart

```bash
cd /pfad/zu/scan-for-dirty-git-repos-gui
./autostart-install.sh
```

That's it! The application will now start automatically every time you log in.

## What Gets Installed

The installation script creates:

1. **Desktop Entry for Autostart**
   - Location: `~/.config/autostart/dirty-git-finder.desktop`
   - Makes the app start automatically at login
   - Generated dynamically with correct paths

2. **Application Menu Entry**
   - Location: `~/.local/share/applications/dirty-git-finder.desktop`
   - Adds the app to your applications menu

3. **CLI Symlink**
   - Location: `~/.local/bin/dirty-git-finder`
   - Allows launching from terminal with `dirty-git-finder`

4. **Executable Scripts**
   - Makes `launch.sh`, `run.py`, and `dirty_git_finder.py` executable

## Files

- `launch.sh` - Shell script that launches the application
- `dirty-git-finder.desktop` - Desktop entry template file
- `autostart-install.sh` - Installation script
- `uninstall-autostart.sh` - Uninstallation script

## Managing Autostart

### Check if Autostart is Enabled

```bash
ls ~/.config/autostart/dirty-git-finder.desktop
```

If the file exists, autostart is enabled.

### Disable Autostart (Temporarily)

```bash
rm ~/.config/autostart/dirty-git-finder.desktop
```

The app will still be in your applications menu, but won't start automatically.

### Re-enable Autostart

```bash
./autostart-install.sh
```

### Completely Uninstall Autostart

```bash
./uninstall-autostart.sh
```

This removes both the autostart entry and the application menu entry.

### Toggle via GUI

You can also enable/disable autostart directly in the application:
- Open Dirty Git Finder
- Check/uncheck "Beim Systemstart ausführen" checkbox

## Manual Launch

If you want to start the application manually:

```bash
# Method 1: Using the CLI symlink (if in PATH)
dirty-git-finder

# Method 2: Using the launch script
./launch.sh

# Method 3: Using Python directly
python3 run.py

# Method 4: Direct execution
python3 dirty_git_finder.py
```

## Troubleshooting

### Application doesn't start at login

1. Check if the desktop entry exists:
   ```bash
   cat ~/.config/autostart/dirty-git-finder.desktop
   ```

2. Verify the paths in the desktop entry point to existing files

3. Make sure the scripts are executable:
   ```bash
   ls -l launch.sh run.py dirty_git_finder.py
   ```
   All should have `x` permission.

4. Try running the launcher manually:
   ```bash
   ./launch.sh
   ```
   Check for any error messages.

### Multiple instances starting

This can happen if you've set up autostart multiple ways. Check:

```bash
# Check autostart directory
ls ~/.config/autostart/

# Check for duplicate entries
grep -r "dirty_git_finder" ~/.config/autostart/
```

### Application starts but crashes immediately

Enable logging by editing `launch.sh` and uncommenting the log line:

```bash
echo "$(date): Dirty Git Finder started" >> "$HOME/.local/share/dirty-git-finder/startup.log"
```

Then check the log:
```bash
cat ~/.local/share/dirty-git-finder/startup.log
```

## Desktop Environment Compatibility

This autostart method works with:
- GNOME
- KDE Plasma
- XFCE
- MATE
- Cinnamon
- Most other XDG-compliant desktop environments

## Advanced Configuration

### Change Start Delay

Edit `~/.config/autostart/dirty-git-finder.desktop` and add:

```ini
X-GNOME-Autostart-Delay=10
```

This delays start by 10 seconds (useful if you want other apps to start first).

### Start Minimized

Edit `launch.sh` to pass any startup options your application supports.

## Security Notes

- The application only reads Git repository information
- No sensitive data is written or transmitted
- All operations are local to your system
- The application runs with your user permissions

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Run the application manually to see error messages
3. Check system logs: `journalctl --user -xe`
