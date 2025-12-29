#!/usr/bin/env python3
"""
Dirty Git Repository Finder GUI
A Python GUI application that scans the home directory for Git repositories
and identifies which ones have uncommitted changes (are "dirty").
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os
import subprocess
import threading
from pathlib import Path
import queue


class GitRepoScanner:
    """Handles scanning for Git repositories and checking their status."""
    
    def __init__(self):
        self.scan_cancelled = False
    
    def is_git_repo(self, path):
        """Check if a directory is a Git repository."""
        git_dir = os.path.join(path, '.git')
        return os.path.exists(git_dir)
    
    def is_repo_dirty(self, repo_path):
        """Check if a Git repository has uncommitted changes."""
        try:
            # Change to the repository directory
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            # If there's output, the repo is dirty
            return bool(result.stdout.strip())
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def get_repo_status(self, repo_path):
        """Get detailed status information for a Git repository."""
        try:
            # Get branch name
            branch_result = subprocess.run(
                ['git', 'branch', '--show-current'],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=5
            )
            branch = branch_result.stdout.strip() or "detached HEAD"
            
            # Get status summary
            status_result = subprocess.run(
                ['git', 'status', '--porcelain'],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            status_lines = status_result.stdout.strip().split('\n') if status_result.stdout.strip() else []
            
            # Get oldest modification time of dirty files
            oldest_mod_time = self.get_oldest_dirty_file_time(repo_path, status_lines)
            
            # Get last commit info
            last_commit_info = self.get_last_commit_info(repo_path)
            
            return {
                'branch': branch,
                'dirty': bool(status_lines),
                'changes_count': len(status_lines),
                'changes': status_lines[:5],  # Show first 5 changes
                'oldest_modification': oldest_mod_time,
                'last_commit': last_commit_info
            }
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
            return {'branch': 'unknown', 'dirty': False, 'changes_count': 0, 'changes': [], 'oldest_modification': None, 'last_commit': None}
    
    def get_oldest_dirty_file_time(self, repo_path, status_lines):
        """Get the oldest modification time of dirty files with filename."""
        if not status_lines:
            return None
            
        import datetime
        oldest_time = None
        oldest_filename = None
        
        try:
            for line in status_lines[:10]:  # Check first 10 files to avoid performance issues
                if len(line) < 3:
                    continue
                    
                filename = line[3:].strip()
                file_path = os.path.join(repo_path, filename)
                
                try:
                    if os.path.exists(file_path):
                        mod_time = os.path.getmtime(file_path)
                        if oldest_time is None or mod_time < oldest_time:
                            oldest_time = mod_time
                            oldest_filename = filename
                except OSError:
                    continue
            
            if oldest_time and oldest_filename:
                # Get just the filename without path
                basename = os.path.basename(oldest_filename)
                
                # Truncate filename to max 15 characters with ...
                if len(basename) > 15:
                    display_name = basename[:12] + "..."
                else:
                    display_name = basename
                
                time_str = self.format_relative_time(oldest_time)
                return {
                    'display': f"{display_name} ({time_str})",
                    'timestamp': oldest_time
                }
            
        except Exception:
            pass
            
        return None
    
    def format_relative_time(self, timestamp):
        """Format timestamp as relative time or German date format."""
        import datetime
        
        mod_time = datetime.datetime.fromtimestamp(timestamp)
        now = datetime.datetime.now()
        diff = now - mod_time
        
        # Wenn weniger als 24 Stunden alt, zeige relative Zeit
        if diff.total_seconds() < 86400:  # 24 Stunden
            hours = int(diff.total_seconds() // 3600)
            minutes = int((diff.total_seconds() % 3600) // 60)
            
            if hours > 0:
                return f"vor {hours} Std."
            elif minutes > 0:
                return f"vor {minutes} Min."
            else:
                return "gerade eben"
        
        # Wenn heute, zeige nur Zeit
        if mod_time.date() == now.date():
            return f"heute {mod_time.strftime('%H:%M')}"
        
        # Wenn gestern
        yesterday = now.date() - datetime.timedelta(days=1)
        if mod_time.date() == yesterday:
            return f"gestern {mod_time.strftime('%H:%M')}"
        
        # Wenn diese Woche
        if diff.days < 7:
            weekdays = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
            weekday = weekdays[mod_time.weekday()]
            return f"{weekday} {mod_time.strftime('%H:%M')}"
        
        # Sonst deutsches Datumsformat
        return mod_time.strftime('%d.%m.%Y %H:%M')
    
    def get_last_commit_info(self, repo_path):
        """Get information about the last commit."""
        try:
            # Get last commit timestamp
            result = subprocess.run(
                ['git', 'log', '-1', '--format=%ct'],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0 and result.stdout.strip():
                commit_timestamp = int(result.stdout.strip())
                formatted_time = self.format_relative_time(commit_timestamp)
                
                return {
                    'timestamp': commit_timestamp,
                    'display': formatted_time
                }
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, ValueError):
            pass
        
        return None
    
    def calculate_time_diff(self, oldest_mod_info, last_commit_info):
        """Calculate time difference between last commit and oldest modification."""
        if not oldest_mod_info or not last_commit_info:
            return ''
        
        try:
            # Get timestamps
            if isinstance(oldest_mod_info, dict) and 'timestamp' in oldest_mod_info:
                mod_timestamp = oldest_mod_info['timestamp']
            else:
                return ''
                
            if isinstance(last_commit_info, dict) and 'timestamp' in last_commit_info:
                commit_timestamp = last_commit_info['timestamp']
            else:
                return ''
            
            # Calculate difference (commit time - modification time)
            # Positive means commit is newer than modification
            diff_seconds = commit_timestamp - mod_timestamp
            
            if diff_seconds >= 0:
                return 'nach Commit'
            
            # Convert to human readable format (how long since last commit)
            abs_diff = abs(diff_seconds)
            diff_minutes = int(abs_diff // 60)
            diff_hours = int(diff_minutes // 60)
            diff_days = int(diff_hours // 24)
            
            if diff_days > 0:
                return f"{diff_days}d alt"
            elif diff_hours > 0:
                return f"{diff_hours}h alt"
            elif diff_minutes > 0:
                return f"{diff_minutes}m alt"
            else:
                return "<1m alt"
                
        except (ValueError, TypeError):
            return ''
    
    def scan_directory(self, start_path, progress_callback=None, result_callback=None):
        """Scan directory tree for Git repositories."""
        found_repos = []
        self.scan_cancelled = False
        
        try:
            for root, dirs, files in os.walk(start_path):
                if self.scan_cancelled:
                    break
                
                # Skip common non-repository directories
                dirs[:] = [d for d in dirs if not d.startswith('.') or d == '.git']
                
                if self.is_git_repo(root):
                    repo_info = {
                        'path': root,
                        'name': os.path.basename(root),
                        **self.get_repo_status(root)
                    }
                    found_repos.append(repo_info)
                    
                    if result_callback:
                        result_callback(repo_info)
                
                if progress_callback:
                    progress_callback(root)
        
        except PermissionError:
            pass  # Skip directories we can't access
        
        return found_repos
    
    def cancel_scan(self):
        """Cancel the current scan operation."""
        self.scan_cancelled = True


class DirtyGitFinderGUI:
    """Main GUI application class."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Dirty Git Repository Finder")
        self.root.geometry("1000x700")
        
        self.scanner = GitRepoScanner()
        self.scan_thread = None
        self.found_repos = []
        
        self.setup_ui()
        
        # Automatisch Home-Verzeichnis scannen nach UI-Setup
        self.root.after(100, self.auto_start_scan)
        
    def setup_ui(self):
        """Set up the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Scan path selection
        ttk.Label(main_frame, text="Scan Path:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        path_frame = ttk.Frame(main_frame)
        path_frame.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=(0, 5))
        path_frame.columnconfigure(0, weight=1)
        
        self.path_var = tk.StringVar(value=str(Path.home()))
        self.path_entry = ttk.Entry(path_frame, textvariable=self.path_var)
        self.path_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        
        ttk.Button(path_frame, text="Browse", command=self.browse_path).grid(row=0, column=1)
        
        # Control buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.scan_button = ttk.Button(button_frame, text="Start Scan", command=self.start_scan)
        self.scan_button.pack(side=tk.LEFT, padx=(0, 5))
        
        self.cancel_button = ttk.Button(button_frame, text="Cancel", command=self.cancel_scan, state='disabled')
        self.cancel_button.pack(side=tk.LEFT, padx=(0, 5))
        
        self.clear_button = ttk.Button(button_frame, text="Clear Results", command=self.clear_results)
        self.clear_button.pack(side=tk.LEFT)
        
        # Progress bar
        self.progress_var = tk.StringVar(value="Ready to scan")
        ttk.Label(main_frame, textvariable=self.progress_var).grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))
        
        # Results area
        results_frame = ttk.LabelFrame(main_frame, text="Git Repositories Found", padding="5")
        results_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(5, 0))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        # Treeview for results
        columns = ('Name', 'Path', 'Branch', 'Status', 'Changes', 'Last Modified', 'Last Commit', 'Time Diff')
        self.tree = ttk.Treeview(results_frame, columns=columns, show='headings', height=15)
        
        # Configure columns with sorting
        self.sort_column = None
        self.sort_reverse = False
        
        self.tree.heading('Name', text='Repository Name', command=lambda: self.sort_treeview('Name', 'alpha'))
        self.tree.heading('Path', text='Path', command=lambda: self.sort_treeview('Path', 'alpha'))
        self.tree.heading('Branch', text='Branch', command=lambda: self.sort_treeview('Branch', 'alpha'))
        self.tree.heading('Status', text='Status', command=lambda: self.sort_treeview('Status', 'alpha'))
        self.tree.heading('Changes', text='Changes', command=lambda: self.sort_treeview('Changes', 'numeric'))
        self.tree.heading('Last Modified', text='Älteste Änderung', command=lambda: self.sort_treeview('Last Modified', 'date'))
        self.tree.heading('Last Commit', text='Letzter Commit', command=lambda: self.sort_treeview('Last Commit', 'date'))
        self.tree.heading('Time Diff', text='Zeitdifferenz', command=lambda: self.sort_treeview('Time Diff', 'timediff'))
        
        self.tree.column('Name', width=130)
        self.tree.column('Path', width=170)
        self.tree.column('Branch', width=80)
        self.tree.column('Status', width=90)
        self.tree.column('Changes', width=60)
        self.tree.column('Last Modified', width=160)
        self.tree.column('Last Commit', width=140)
        self.tree.column('Time Diff', width=90)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(results_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Grid treeview and scrollbars
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Configure tags for branch highlighting (entire row)
        self.tree.tag_configure('non_main_branch', foreground='red', background='#ffe6e6', font=('TkDefaultFont', 10, 'bold'))

        # Bind events
        self.tree.bind('<Double-1>', self.on_double_click)
        self.tree.bind('<Button-3>', self.on_right_click)  # Right click
        self.tree.bind('<Button-1>', self.on_single_click)  # Single click for git graph
        
        # Create context menu
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Git Graph anzeigen", command=self.show_git_graph)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="🔄 Push & Pull ausführen", command=self.git_push_pull)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Remote URL in Browser öffnen", command=self.open_remote_url)
        self.context_menu.add_command(label="Im Datei-Explorer öffnen", command=self.open_in_file_browser)
        self.context_menu.add_command(label="In VS Code öffnen", command=self.open_in_vscode)
        self.context_menu.add_command(label="Terminal öffnen", command=self.open_terminal)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="🔧 Open *this* Project", command=self.open_this_project)
        
        # Bind events to hide context menu
        self.root.bind('<Button-1>', self.hide_context_menu)  # Left click anywhere
        self.root.bind('<Button-3>', self.hide_context_menu)  # Right click anywhere (except on tree)
        self.root.bind('<Key-Escape>', self.hide_context_menu)  # Escape key
        self.root.bind('<FocusOut>', self.hide_context_menu)  # Window loses focus
        main_frame.bind('<Button-1>', self.hide_context_menu)
        self.tree.bind('<Button-1>', self.hide_context_menu)
        
        # Make sure the root window can receive key events
        self.root.focus_set()
        
        # Status bar
        self.status_var = tk.StringVar(value="Wird geladen...")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(5, 0))
        
        # Filter frame
        filter_frame = ttk.LabelFrame(main_frame, text="Filter & Optionen", padding="5")
        filter_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(5, 0))
        
        # Filter options
        filter_left = ttk.Frame(filter_frame)
        filter_left.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        ttk.Label(filter_left, text="Show:").pack(side=tk.LEFT)
        
        self.filter_var = tk.StringVar(value="dirty")  # Dirty Only als Standard
        ttk.Radiobutton(filter_left, text="All", variable=self.filter_var, value="all", command=self.apply_filter).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Radiobutton(filter_left, text="Dirty Only", variable=self.filter_var, value="dirty", command=self.apply_filter).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Radiobutton(filter_left, text="Clean Only", variable=self.filter_var, value="clean", command=self.apply_filter).pack(side=tk.LEFT, padx=(5, 0))
        
        # Separator
        ttk.Separator(filter_frame, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=(10, 10))
        
        # Autostart option
        filter_right = ttk.Frame(filter_frame)
        filter_right.pack(side=tk.RIGHT)
        
        self.autostart_var = tk.BooleanVar()
        self.autostart_checkbox = ttk.Checkbutton(
            filter_right, 
            text="Beim Systemstart ausführen", 
            variable=self.autostart_var,
            command=self.toggle_autostart
        )
        self.autostart_checkbox.pack(side=tk.RIGHT)
        
        # Check current autostart status
        self.check_autostart_status()
        
    def browse_path(self):
        """Browse for a directory to scan."""
        from tkinter import filedialog
        directory = filedialog.askdirectory(initialdir=self.path_var.get())
        if directory:
            self.path_var.set(directory)
    
    def start_scan(self):
        """Start scanning for Git repositories."""
        scan_path = self.path_var.get()
        if not os.path.exists(scan_path):
            messagebox.showerror("Error", "Selected path does not exist!")
            return
        
        self.found_repos.clear()
        self.clear_results()
        
        self.scan_button.config(state='disabled')
        self.cancel_button.config(state='normal')
        self.progress_var.set("Scanning...")
        self.status_var.set("Scan in progress...")
        
        # Start scan in separate thread
        self.scan_thread = threading.Thread(
            target=self._scan_worker,
            args=(scan_path,),
            daemon=True
        )
        self.scan_thread.start()
    
    def _scan_worker(self, scan_path):
        """Worker thread for scanning repositories."""
        def progress_callback(current_path):
            self.root.after(0, lambda: self.progress_var.set(f"Scanning: {current_path}"))
        
        def result_callback(repo_info):
            self.found_repos.append(repo_info)
            self.root.after(0, lambda: self._add_repo_to_tree(repo_info))
        
        try:
            repos = self.scanner.scan_directory(
                scan_path,
                progress_callback=progress_callback,
                result_callback=result_callback
            )
            
            self.root.after(0, self._scan_completed)
            
        except Exception as e:
            self.root.after(0, lambda: self._scan_error(str(e)))
    
    def _add_repo_to_tree(self, repo_info):
        """Add a repository to the results tree."""
        status = "🔥 DIRTY" if repo_info['dirty'] else "✅ CLEAN"
        status_color = "red" if repo_info['dirty'] else "green"
        oldest_mod_info = repo_info.get('oldest_modification', '')
        last_commit_info = repo_info.get('last_commit', '')
        
        # Handle both string and dict format for oldest_modification
        if isinstance(oldest_mod_info, dict):
            oldest_mod_display = oldest_mod_info.get('display', '')
        else:
            oldest_mod_display = oldest_mod_info or ''
        
        # Handle last commit display
        if isinstance(last_commit_info, dict):
            last_commit_display = last_commit_info.get('display', '')
        else:
            last_commit_display = last_commit_info or ''
        
        # Calculate time difference
        time_diff = self.scanner.calculate_time_diff(oldest_mod_info, last_commit_info)

        # Insert dirty repos at the beginning, clean repos at the end
        position = 0 if repo_info['dirty'] else 'end'

        # Determine tags for branch highlighting
        branch = repo_info['branch']
        tags = ()
        if branch not in ('main', 'master'):
            tags = ('non_main_branch',)

        item = self.tree.insert('', position, values=(
            repo_info['name'],
            repo_info['path'],
            repo_info['branch'],
            status,
            repo_info['changes_count'],
            oldest_mod_display,
            last_commit_display,
            time_diff
        ), tags=tags)

        # Color code dirty repositories
        if repo_info['dirty']:
            self.tree.set(item, 'Status', status)
    
    def _scan_completed(self):
        """Handle scan completion."""
        self.scan_button.config(state='normal')
        self.cancel_button.config(state='disabled')
        
        total_repos = len(self.found_repos)
        dirty_repos = sum(1 for repo in self.found_repos if repo['dirty'])
        
        self.progress_var.set(f"Scan completed - Found {total_repos} repositories")
        self.status_var.set(f"Total: {total_repos} repositories, Dirty: {dirty_repos}, Clean: {total_repos - dirty_repos}")
        
        self.apply_filter()
    
    def _scan_error(self, error_msg):
        """Handle scan error."""
        self.scan_button.config(state='normal')
        self.cancel_button.config(state='disabled')
        self.progress_var.set("Scan failed")
        self.status_var.set(f"Error: {error_msg}")
        messagebox.showerror("Scan Error", f"An error occurred during scanning:\n{error_msg}")
    
    def cancel_scan(self):
        """Cancel the current scan."""
        self.scanner.cancel_scan()
        self.scan_button.config(state='normal')
        self.cancel_button.config(state='disabled')
        self.progress_var.set("Scan cancelled")
        self.status_var.set("Scan was cancelled by user")
    
    def clear_results(self):
        """Clear the results tree."""
        for item in self.tree.get_children():
            self.tree.delete(item)
    
    def on_double_click(self, event):
        """Handle double-click on repository entry."""
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            repo_path = self.tree.item(item, 'values')[1]  # Path is in column 1
            self.open_folder_in_file_manager(repo_path)
    
    def on_right_click(self, event):
        """Handle right-click on repository entry."""
        # Hide any existing context menu first
        self.hide_context_menu()
        
        # Select the item under cursor
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)
            
            # Stop event propagation to prevent immediate hiding
            return "break"
    
    def get_selected_repo_path(self):
        """Get the path of the currently selected repository."""
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            return self.tree.item(item, 'values')[1]  # Path is in column 1
        return None
    
    def open_folder_in_file_manager(self, path):
        """Open folder in the system's file manager."""
        import platform
        try:
            system = platform.system()
            if system == "Linux":
                subprocess.Popen(['xdg-open', path])
            elif system == "Darwin":  # macOS
                subprocess.Popen(['open', path])
            elif system == "Windows":
                subprocess.Popen(['explorer', path])
        except Exception as e:
            messagebox.showerror("Fehler", f"Konnte Ordner nicht öffnen: {e}")
    
    def open_remote_url(self):
        """Open the remote URL of the selected repository in browser."""
        repo_path = self.get_selected_repo_path()
        if not repo_path:
            return
        
        try:
            # Get remote URL
            result = subprocess.run(
                ['git', 'remote', 'get-url', 'origin'],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                remote_url = result.stdout.strip()
                
                # Convert SSH URLs to HTTPS
                if remote_url.startswith('git@'):
                    # git@github.com:user/repo.git -> https://github.com/user/repo
                    remote_url = remote_url.replace(':', '/').replace('git@', 'https://')
                    if remote_url.endswith('.git'):
                        remote_url = remote_url[:-4]
                
                # Open in browser
                import webbrowser
                webbrowser.open(remote_url)
            else:
                messagebox.showwarning("Warnung", "Kein Remote-Repository gefunden.")
                
        except Exception as e:
            messagebox.showerror("Fehler", f"Konnte Remote-URL nicht öffnen: {e}")
    
    def open_in_file_browser(self):
        """Open the selected repository in file browser."""
        repo_path = self.get_selected_repo_path()
        if repo_path:
            self.open_folder_in_file_manager(repo_path)
    
    def open_in_vscode(self):
        """Open the selected repository in VS Code."""
        repo_path = self.get_selected_repo_path()
        if not repo_path:
            return

        try:
            # Try to open in VS Code
            subprocess.Popen(['code', repo_path])
        except FileNotFoundError:
            # VS Code not found, try with different command
            try:
                subprocess.Popen(['code-insiders', repo_path])
            except FileNotFoundError:
                messagebox.showerror("Fehler", "VS Code ist nicht installiert oder nicht im PATH verfügbar.")

    def open_terminal(self):
        """Open a terminal in the selected repository directory."""
        repo_path = self.get_selected_repo_path()
        if not repo_path:
            return

        try:
            import platform
            system = platform.system()

            if system == "Linux":
                # Try common Linux terminals
                terminals = [
                    ['gnome-terminal', '--working-directory=' + repo_path],
                    ['konsole', '--workdir', repo_path],
                    ['xfce4-terminal', '--working-directory=' + repo_path],
                    ['xterm', '-e', f'cd "{repo_path}" && bash'],
                ]

                terminal_opened = False
                for terminal_cmd in terminals:
                    try:
                        subprocess.Popen(terminal_cmd)
                        terminal_opened = True
                        break
                    except FileNotFoundError:
                        continue

                if not terminal_opened:
                    messagebox.showerror("Fehler", "Kein Terminal-Emulator gefunden.")

            elif system == "Darwin":  # macOS
                # Use Terminal.app on macOS
                script = f'tell application "Terminal" to do script "cd \\"{repo_path}\\""'
                subprocess.Popen(['osascript', '-e', script])

            elif system == "Windows":
                # Use cmd on Windows
                subprocess.Popen(['cmd', '/K', 'cd', '/D', repo_path])

        except Exception as e:
            messagebox.showerror("Fehler", f"Terminal konnte nicht geöffnet werden: {e}")

    def open_this_project(self):
        """Open this project (the GUI tool itself) in VS Code."""
        # Get the directory where this script is located
        this_project_path = os.path.dirname(os.path.abspath(__file__))

        try:
            # Try to open in VS Code
            subprocess.Popen(['code', this_project_path])
        except FileNotFoundError:
            # VS Code not found, try with different command
            try:
                subprocess.Popen(['code-insiders', this_project_path])
            except FileNotFoundError:
                # Fall back to file browser
                self.open_folder_in_file_manager(this_project_path)

    def git_push_pull(self):
        """Execute git pull and push for the selected repository."""
        repo_path = self.get_selected_repo_path()
        if not repo_path:
            return

        try:
            # Create a new window to show the output
            output_window = tk.Toplevel(self.root)
            output_window.title(f"Git Push & Pull - {os.path.basename(repo_path)}")
            output_window.geometry("700x500")

            # Create text widget with scrollbars
            frame = ttk.Frame(output_window)
            frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            # Text widget for output
            text_widget = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=('Courier', 10))
            text_widget.pack(fill=tk.BOTH, expand=True)

            def run_git_commands():
                """Run git pull and push in a separate thread."""
                try:
                    # Git Pull
                    text_widget.insert(tk.END, "=== Git Pull ===\n")
                    text_widget.update_idletasks()

                    pull_result = subprocess.run(
                        ['git', 'pull'],
                        cwd=repo_path,
                        capture_output=True,
                        text=True,
                        timeout=30
                    )

                    text_widget.insert(tk.END, pull_result.stdout)
                    if pull_result.stderr:
                        text_widget.insert(tk.END, pull_result.stderr)
                    text_widget.insert(tk.END, f"\nExit Code: {pull_result.returncode}\n\n")
                    text_widget.update_idletasks()

                    # Git Push
                    text_widget.insert(tk.END, "=== Git Push ===\n")
                    text_widget.update_idletasks()

                    push_result = subprocess.run(
                        ['git', 'push'],
                        cwd=repo_path,
                        capture_output=True,
                        text=True,
                        timeout=30
                    )

                    text_widget.insert(tk.END, push_result.stdout)
                    if push_result.stderr:
                        text_widget.insert(tk.END, push_result.stderr)
                    text_widget.insert(tk.END, f"\nExit Code: {push_result.returncode}\n\n")

                    # Summary
                    if pull_result.returncode == 0 and push_result.returncode == 0:
                        text_widget.insert(tk.END, "✅ Push & Pull erfolgreich abgeschlossen!\n")
                    else:
                        text_widget.insert(tk.END, "⚠️ Es gab Fehler oder Warnungen.\n")

                    text_widget.update_idletasks()

                except subprocess.TimeoutExpired:
                    text_widget.insert(tk.END, "\n❌ Timeout: Git-Befehl dauerte zu lange.\n")
                except Exception as e:
                    text_widget.insert(tk.END, f"\n❌ Fehler: {str(e)}\n")

                # Make text read-only
                text_widget.config(state=tk.DISABLED)

            # Run in separate thread to avoid blocking UI
            import threading
            git_thread = threading.Thread(target=run_git_commands, daemon=True)
            git_thread.start()

            # Add close button
            close_button = ttk.Button(output_window, text="Schließen", command=output_window.destroy)
            close_button.pack(pady=(5, 10))

        except Exception as e:
            messagebox.showerror("Fehler", f"Konnte Push & Pull nicht ausführen: {e}")
    
    def auto_start_scan(self):
        """Automatically start scanning the home directory."""
        home_path = str(Path.home())
        self.path_var.set(home_path)
        self.status_var.set("Automatischer Scan wird gestartet...")
        
        # Kurz warten damit UI vollständig geladen ist
        self.root.after(200, self.start_scan)
    
    def hide_context_menu(self, event=None):
        """Hide the context menu."""
        try:
            self.context_menu.unpost()
        except:
            pass  # Menu might not be posted
    
    def get_repo_oldest_timestamp(self, repo_info):
        """Extract timestamp from repository info for sorting."""
        if not repo_info.get('dirty', False):
            return 9999999999  # Clean repos get high timestamp (sorted last)
        
        # First try to get timestamp from stored data
        oldest_mod_info = repo_info.get('oldest_modification', {})
        if isinstance(oldest_mod_info, dict) and 'timestamp' in oldest_mod_info:
            return oldest_mod_info['timestamp']
        
        # Fallback: calculate directly from repo path
        try:
            repo_path = repo_info.get('path', '')
            if repo_path:
                oldest_timestamp = self.calculate_oldest_timestamp_direct(repo_path)
                return oldest_timestamp if oldest_timestamp else 9999999999
        except Exception:
            pass
        
        return 9999999999  # Fallback
    
    def calculate_oldest_timestamp_direct(self, repo_path):
        """Calculate oldest timestamp directly from git status files."""
        try:
            # Get git status
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode != 0:
                return None
                
            status_lines = [line for line in result.stdout.strip().split('\n') if line.strip()]
            if not status_lines:
                return None
            
            oldest_time = None
            
            for line in status_lines[:10]:  # Check first 10 files
                if len(line) < 3:
                    continue
                    
                filename = line[3:].strip()
                file_path = os.path.join(repo_path, filename)
                
                try:
                    if os.path.exists(file_path):
                        mod_time = os.path.getmtime(file_path)
                        if oldest_time is None or mod_time < oldest_time:
                            oldest_time = mod_time
                except OSError:
                    continue
            
            return oldest_time
            
        except Exception:
            return None
    
    def on_single_click(self, event):
        """Handle single click on repository entry to show git info."""
        # Don't interfere with context menu hiding
        if hasattr(self, '_ignore_click'):
            return
        
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            repo_path = self.tree.item(item, 'values')[1]  # Path is in column 1
            # Show git graph in a small popup or status area
            self.show_git_info_brief(repo_path)
    
    def show_git_info_brief(self, repo_path):
        """Show brief git information in the status bar."""
        try:
            # Get last commit info
            result = subprocess.run(
                ['git', 'log', '--oneline', '-1'],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=3
            )
            
            if result.returncode == 0:
                last_commit = result.stdout.strip()
                self.status_var.set(f"Letzter Commit: {last_commit}")
            else:
                self.status_var.set("Keine Commit-Informationen verfügbar")
                
        except Exception as e:
            self.status_var.set(f"Git-Info nicht verfügbar: {str(e)}")
    
    def show_git_graph(self):
        """Show git graph in a new window."""
        repo_path = self.get_selected_repo_path()
        if not repo_path:
            return
        
        try:
            # Create new window for git graph
            graph_window = tk.Toplevel(self.root)
            graph_window.title(f"Git Graph - {os.path.basename(repo_path)}")
            graph_window.geometry("800x600")
            
            # Create text widget with scrollbars
            frame = ttk.Frame(graph_window)
            frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Text widget for git log
            text_widget = scrolledtext.ScrolledText(frame, wrap=tk.NONE, font=('Courier', 10))
            text_widget.pack(fill=tk.BOTH, expand=True)
            
            # Get git log with graph
            result = subprocess.run(
                ['git', 'log', '--graph', '--pretty=format:%h -%d %s (%cr) <%an>', '--abbrev-commit', '-20'],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                git_output = result.stdout
                text_widget.insert(tk.END, git_output)
            else:
                text_widget.insert(tk.END, "Fehler beim Laden des Git-Graphs")
            
            # Make text read-only
            text_widget.config(state=tk.DISABLED)
            
            # Add close button
            close_button = ttk.Button(graph_window, text="Schließen", command=graph_window.destroy)
            close_button.pack(pady=(5, 10))
            
        except Exception as e:
            messagebox.showerror("Fehler", f"Konnte Git-Graph nicht anzeigen: {e}")
    
    def sort_treeview(self, column, sort_type):
        """Sort treeview by column with different sorting methods."""
        # Toggle sort order if same column clicked again
        if self.sort_column == column:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_reverse = False
            self.sort_column = column
        
        # Get column index
        columns = list(self.tree['columns'])
        col_index = columns.index(column)
        
        # Get all items with their values
        items = [(self.tree.item(child)['values'], child) for child in self.tree.get_children()]
        
        # Sort based on column type
        if sort_type == 'alpha':
            items.sort(key=lambda x: str(x[0][col_index]).lower(), reverse=self.sort_reverse)
        elif sort_type == 'numeric':
            items.sort(key=lambda x: self._extract_numeric(x[0][col_index]), reverse=self.sort_reverse)
        elif sort_type == 'date':
            items.sort(key=lambda x: self._extract_date_timestamp(x[0][col_index]), reverse=self.sort_reverse)
        elif sort_type == 'timediff':
            items.sort(key=lambda x: self._extract_timediff_value(x[0][col_index]), reverse=self.sort_reverse)
        
        # Rearrange items in tree
        for index, (values, item) in enumerate(items):
            self.tree.move(item, '', index)
        
        # Update column heading to show sort direction
        self._update_column_headers(column)
    
    def _extract_numeric(self, value):
        """Extract numeric value for sorting."""
        try:
            return int(str(value))
        except (ValueError, TypeError):
            return 0
    
    def _extract_date_timestamp(self, value):
        """Extract timestamp from date string for sorting."""
        if not value:
            return 0
        
        value_str = str(value)
        import datetime, re
        
        try:
            # Try to extract from formatted display like "config.py (vor 2 Std.)"
            if '(' in value_str and ')' in value_str:
                time_part = value_str.split('(')[1].split(')')[0]
            else:
                time_part = value_str
            
            now = datetime.datetime.now()
            
            # Parse different time formats
            if 'gerade eben' in time_part:
                return now.timestamp()
            elif 'vor' in time_part and 'Min.' in time_part:
                minutes = int(re.findall(r'vor (\d+) Min\.', time_part)[0])
                return (now - datetime.timedelta(minutes=minutes)).timestamp()
            elif 'vor' in time_part and 'Std.' in time_part:
                hours = int(re.findall(r'vor (\d+) Std\.', time_part)[0])
                return (now - datetime.timedelta(hours=hours)).timestamp()
            elif 'heute' in time_part:
                time_match = re.findall(r'heute (\d{2}:\d{2})', time_part)
                if time_match:
                    time_obj = datetime.datetime.strptime(time_match[0], '%H:%M').time()
                    return datetime.datetime.combine(now.date(), time_obj).timestamp()
            elif 'gestern' in time_part:
                time_match = re.findall(r'gestern (\d{2}:\d{2})', time_part)
                if time_match:
                    yesterday = now.date() - datetime.timedelta(days=1)
                    time_obj = datetime.datetime.strptime(time_match[0], '%H:%M').time()
                    return datetime.datetime.combine(yesterday, time_obj).timestamp()
            elif re.match(r'\d{2}\.\d{2}\.\d{4}', time_part):
                date_match = re.findall(r'(\d{2})\.(\d{2})\.(\d{4}) (\d{2}:\d{2})', time_part)
                if date_match:
                    day, month, year, time_str = date_match[0]
                    dt_str = f"{year}-{month}-{day} {time_str}"
                    return datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M').timestamp()
            
        except (ValueError, IndexError):
            pass
        
        return 0
    
    def _extract_timediff_value(self, value):
        """Extract numeric value from time difference for sorting."""
        if not value:
            return 0
        
        value_str = str(value)
        
        # Handle special cases
        if 'nach Commit' in value_str:
            return -1  # Sort before all others
        
        # Extract numeric value and unit
        try:
            import re
            if 'd alt' in value_str:
                days = int(re.findall(r'(\d+)d alt', value_str)[0])
                return days * 24 * 60  # Convert to minutes
            elif 'h alt' in value_str:
                hours = int(re.findall(r'(\d+)h alt', value_str)[0])
                return hours * 60  # Convert to minutes
            elif 'm alt' in value_str:
                minutes = int(re.findall(r'(\d+)m alt', value_str)[0])
                return minutes
            elif '<1m alt' in value_str:
                return 0.5  # Less than 1 minute
        except (ValueError, IndexError):
            pass
        
        return 0
    
    def _update_column_headers(self, sorted_column):
        """Update column headers to show sort direction."""
        columns = {
            'Name': 'Repository Name',
            'Path': 'Path',
            'Branch': 'Branch',
            'Status': 'Status',
            'Changes': 'Changes',
            'Last Modified': 'Älteste Änderung',
            'Last Commit': 'Letzter Commit',
            'Time Diff': 'Zeitdifferenz'
        }
        
        for col, base_text in columns.items():
            if col == sorted_column:
                arrow = ' ↓' if self.sort_reverse else ' ↑'
                self.tree.heading(col, text=base_text + arrow)
            else:
                self.tree.heading(col, text=base_text)
    
    def check_autostart_status(self):
        """Check if autostart is currently enabled."""
        try:
            import platform
            system = platform.system()
            
            if system == "Linux":
                autostart_dir = os.path.expanduser("~/.config/autostart")
                desktop_file = os.path.join(autostart_dir, "dirty-git-finder.desktop")
                self.autostart_var.set(os.path.exists(desktop_file))
            elif system == "Darwin":  # macOS
                # Check for LaunchAgent
                plist_path = os.path.expanduser("~/Library/LaunchAgents/com.dirtygitfinder.plist")
                self.autostart_var.set(os.path.exists(plist_path))
            elif system == "Windows":
                # Check Windows registry
                try:
                    import winreg
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                                       r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_READ)
                    winreg.QueryValueEx(key, "DirtyGitFinder")
                    self.autostart_var.set(True)
                    winreg.CloseKey(key)
                except (FileNotFoundError, OSError):
                    self.autostart_var.set(False)
        except Exception:
            self.autostart_var.set(False)
    
    def toggle_autostart(self):
        """Toggle autostart functionality."""
        try:
            import platform
            system = platform.system()
            script_path = os.path.abspath(__file__)
            
            if self.autostart_var.get():
                # Enable autostart
                if system == "Linux":
                    self.create_linux_autostart(script_path)
                elif system == "Darwin":
                    self.create_macos_autostart(script_path)
                elif system == "Windows":
                    self.create_windows_autostart(script_path)
                
                messagebox.showinfo("Autostart", "Programm wurde für Autostart beim Systemstart aktiviert.")
            else:
                # Disable autostart
                if system == "Linux":
                    self.remove_linux_autostart()
                elif system == "Darwin":
                    self.remove_macos_autostart()
                elif system == "Windows":
                    self.remove_windows_autostart()
                
                messagebox.showinfo("Autostart", "Autostart wurde deaktiviert.")
                
        except Exception as e:
            messagebox.showerror("Fehler", f"Autostart konnte nicht konfiguriert werden: {e}")
            # Reset checkbox on error
            self.check_autostart_status()
    
    def create_linux_autostart(self, script_path):
        """Create Linux autostart entry."""
        autostart_dir = os.path.expanduser("~/.config/autostart")
        os.makedirs(autostart_dir, exist_ok=True)
        
        desktop_content = f"""[Desktop Entry]
Type=Application
Name=Dirty Git Finder
Comment=Git Repository Status Monitor
Exec=python3 "{script_path}"
Icon=git
Terminal=false
Categories=Development;
X-GNOME-Autostart-enabled=true
"""
        
        desktop_file = os.path.join(autostart_dir, "dirty-git-finder.desktop")
        with open(desktop_file, 'w') as f:
            f.write(desktop_content)
        
        # Make executable
        os.chmod(desktop_file, 0o755)
    
    def create_macos_autostart(self, script_path):
        """Create macOS LaunchAgent."""
        launchagents_dir = os.path.expanduser("~/Library/LaunchAgents")
        os.makedirs(launchagents_dir, exist_ok=True)
        
        plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.dirtygitfinder</string>
    <key>ProgramArguments</key>
    <array>
        <string>python3</string>
        <string>{script_path}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <false/>
</dict>
</plist>
"""
        
        plist_path = os.path.join(launchagents_dir, "com.dirtygitfinder.plist")
        with open(plist_path, 'w') as f:
            f.write(plist_content)
    
    def create_windows_autostart(self, script_path):
        """Create Windows autostart registry entry."""
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                               r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, "DirtyGitFinder", 0, winreg.REG_SZ, f'python "{script_path}"')
            winreg.CloseKey(key)
        except Exception as e:
            raise Exception(f"Windows Registry Fehler: {e}")
    
    def remove_linux_autostart(self):
        """Remove Linux autostart entry."""
        desktop_file = os.path.expanduser("~/.config/autostart/dirty-git-finder.desktop")
        if os.path.exists(desktop_file):
            os.remove(desktop_file)
    
    def remove_macos_autostart(self):
        """Remove macOS LaunchAgent."""
        plist_path = os.path.expanduser("~/Library/LaunchAgents/com.dirtygitfinder.plist")
        if os.path.exists(plist_path):
            os.remove(plist_path)
    
    def remove_windows_autostart(self):
        """Remove Windows autostart registry entry."""
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                               r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE)
            winreg.DeleteValue(key, "DirtyGitFinder")
            winreg.CloseKey(key)
        except FileNotFoundError:
            pass  # Already removed
    
    def apply_filter(self):
        """Apply the selected filter to the results."""
        filter_value = self.filter_var.get()
        
        # Clear current display
        self.clear_results()
        
        # Sort repos: dirty first, then by oldest modification time, then by name
        def sort_key(repo):
            # First: dirty repos come first
            if not repo['dirty']:
                return (1, 9999999999, repo['name'].lower())  # Clean repos at the end
            
            # For dirty repos: get timestamp for sorting (oldest first)
            oldest_timestamp = self.get_repo_oldest_timestamp(repo)
            return (0, oldest_timestamp, repo['name'].lower())
        
        sorted_repos = sorted(self.found_repos, key=sort_key)
        
        # Add filtered results
        for repo in sorted_repos:
            if filter_value == "all":
                self._add_repo_to_tree_sorted(repo)
            elif filter_value == "dirty" and repo['dirty']:
                self._add_repo_to_tree_sorted(repo)
            elif filter_value == "clean" and not repo['dirty']:
                self._add_repo_to_tree_sorted(repo)
    
    def _add_repo_to_tree_sorted(self, repo_info):
        """Add a repository to the results tree in sorted order."""
        status = "🔥 DIRTY" if repo_info['dirty'] else "✅ CLEAN"
        oldest_mod_info = repo_info.get('oldest_modification', '')
        last_commit_info = repo_info.get('last_commit', '')
        
        # Handle both string and dict format for oldest_modification
        if isinstance(oldest_mod_info, dict):
            oldest_mod_display = oldest_mod_info.get('display', '')
        else:
            oldest_mod_display = oldest_mod_info or ''
        
        # Handle last commit display
        if isinstance(last_commit_info, dict):
            last_commit_display = last_commit_info.get('display', '')
        else:
            last_commit_display = last_commit_info or ''
        
        # Calculate time difference
        time_diff = self.scanner.calculate_time_diff(oldest_mod_info, last_commit_info)

        # Determine tags for branch highlighting
        branch = repo_info['branch']
        tags = ()
        if branch not in ('main', 'master'):
            tags = ('non_main_branch',)

        item = self.tree.insert('', 'end', values=(
            repo_info['name'],
            repo_info['path'],
            repo_info['branch'],
            status,
            repo_info['changes_count'],
            oldest_mod_display,
            last_commit_display,
            time_diff
        ), tags=tags)

        # Color code dirty repositories
        if repo_info['dirty']:
            self.tree.set(item, 'Status', status)


def main():
    """Main application entry point."""
    root = tk.Tk()
    app = DirtyGitFinderGUI(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()


if __name__ == "__main__":
    main()