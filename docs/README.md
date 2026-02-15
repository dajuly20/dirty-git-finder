# 🔥 Dirty Git Repository Finder GUI

Eine professionelle Python GUI-Anwendung, die Ihr System nach Git-Repositories durchsucht und detailliert anzeigt, welche davon "dirty" sind (uncommitted changes haben). Perfekt für Entwickler, die einen schnellen Überblick über den Status ihrer Projekte benötigen.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)

---

## 📋 Inhaltsverzeichnis

1. [Features](#-features)
2. [Systemvoraussetzungen](#-systemvoraussetzungen)
3. [Installation & Setup](#-installation--setup)
4. [Programmablauf - Detailliert](#-programmablauf---detailliert)
5. [Architektur & Datenfluss](#-architektur--datenfluss)
6. [Projektstruktur](#-projektstruktur)
7. [Bedienungsanleitung](#-bedienungsanleitung)
8. [Troubleshooting](#-troubleshooting)
9. [Entwicklung & Anpassungen](#-entwicklung--anpassungen)

---

## ⭐ Features

### 🔍 **Intelligente Repository-Suche**
- **Rekursive Scan-Engine**: Durchsucht das gesamte Dateisystem nach Git-Repositories
- **Performance-Optimiert**: Überspringt automatisch `.git`, `node_modules`, `__pycache__` etc.
- **Anpassbare Pfade**: Startet im Home-Verzeichnis, aber jeder Pfad wählbar
- **Echtzeit-Updates**: Live-Anzeige der gefundenen Repositories während des Scans

### 🎯 **Erweiterte Git-Status-Analyse**
- **Detaillierte Dirty-Detection**: Erkennt modified, added, deleted, untracked files
- **Einstellbare Dirty-Kriterien**: Checkboxen für Uncommitted changes, No remote, Unpushed commits
- **Remote-Check**: Repositories ohne Remote (GitHub/GitLab) können als DIRTY markiert werden
- **Unpushed-Commits-Detection**: Erkennt Commits die noch nicht gepusht wurden
- **Commit-Timeline**: Zeigt letzten Commit-Zeitpunkt und Alter der Änderungen
- **Branch-Tracking**: Aktueller Branch und HEAD-Status
- **Zeitdifferenz-Analyse**: Wie lange sind Änderungen bereits uncommitted?

### 🖥️ **Professionelle Benutzeroberfläche**
- **Moderne GUI**: Responsive tkinter-Interface mit professionellem Look
- **Emoji-Status**: 🔥 für Dirty, ✅ für Clean Repositories
- **Sortierbare Spalten**: Klicken Sie auf Spalten-Header zum Sortieren
- **Kontextmenü**: Rechtsklick für Git-Graph, VS Code, Datei-Explorer
- **Doppelklick-Integration**: Ordner direkt öffnen

### 📊 **Detaillierte Informationen**
- **Repository Name**: Projekt-Identifikation
- **Vollständiger Pfad**: Exakte Speicherorte
- **Branch Information**: Aktueller Git-Branch
- **Status-Emojis**: Visueller Status auf einen Blick
- **Änderungsanzahl**: Anzahl uncommitted Files
- **Älteste Datei**: Welche Datei wurde zuletzt geändert
- **Letzter Commit**: Wann war der letzte Commit
- **Zeitdifferenz**: Wie alt sind die Änderungen

### ⚡ **Performance & Benutzerfreundlichkeit**
- **Multi-Threading**: UI bleibt responsive während des Scans
- **Abbruch-Funktion**: Scan jederzeit stoppbar
- **Auto-Start**: Beginnt automatisch beim Programmstart
- **Filter-Optionen**: Dirty Only, Clean Only, oder Alle anzeigen
- **Systemstart-Integration**: Optional beim Boot starten

### 🔧 **Entwickler-Tools**
- **Git-Graph-Viewer**: Integrierte Commit-History mit Branching
- **VS Code Integration**: Projekte direkt in VS Code öffnen
- **Remote-URL-Support**: GitHub/GitLab Links direkt im Browser
- **Cross-Platform**: Funktioniert auf Linux, macOS und Windows

---

## 📋 Systemvoraussetzungen

### **Betriebssystem-Unterstützung**
- ✅ **Linux** (Ubuntu, Debian, Fedora, Arch, etc.)
- ✅ **macOS** (10.12+ empfohlen)
- ✅ **Windows** (7, 8, 10, 11)

### **Software-Abhängigkeiten**
- 🐍 **Python 3.7+** (Python 3.8+ empfohlen für beste Performance)
- 📦 **tkinter** (meist mit Python vorinstalliert)
- 🔧 **Git** (muss installiert und im PATH verfügbar sein)

### **System-Spezifische Anforderungen**

#### 🐧 **Linux:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-tk git

# Fedora/CentOS
sudo dnf install python3 python3-tkinter git

# Arch Linux
sudo pacman -S python python-tk git
```

#### 🍎 **macOS:**
```bash
# Mit Homebrew
brew install python-tk git

# Git sollte bereits mit Xcode Command Line Tools installiert sein
xcode-select --install
```

#### 🪟 **Windows:**
- Python von [python.org](https://python.org) herunterladen (tkinter ist enthalten)
- Git von [git-scm.com](https://git-scm.com) installieren
- Beide Programme zu PATH hinzufügen

### **Hardware-Empfehlungen**
- **RAM**: 512 MB+ (für große Repository-Scans)
- **CPU**: Beliebig (optimiert für Single-Core Performance)
- **Speicher**: 50 MB für die Anwendung
- **Bildschirm**: 1024x768+ (1200x800+ empfohlen für beste UX)

---

## 🚀 Installation & Setup

### **Methode 1: Git Clone (Empfohlen)**

```bash
# Repository klonen
git clone https://github.com/dajuly20/scan-for-dirty-git-repos-gui.git
cd scan-for-dirty-git-repos-gui

# System-Check durchführen
python3 --version  # Sollte 3.7+ anzeigen
git --version      # Git sollte verfügbar sein

# Anwendung starten
python3 dirty_git_finder.py
```

### **Methode 2: Direkter Download**

1. **Dateien herunterladen:**
   - Laden Sie `dirty_git_finder.py` und `git_scanner.py` herunter
   - Speichern Sie beide Dateien in einem Ordner

2. **Ausführbar machen (Linux/macOS):**
   ```bash
   chmod +x dirty_git_finder.py
   ```

3. **Starten:**
   ```bash
   python3 dirty_git_finder.py
   # oder direkt:
   ./dirty_git_finder.py
   ```

### **🚀 Autostart Installation**

Das Programm kann automatisch beim Login gestartet werden:

```bash
# Ins Projektverzeichnis wechseln
cd /pfad/zu/scan-for-dirty-git-repos-gui

# Autostart installieren
./autostart-install.sh
```

#### **Was macht die Installation:**
- ✅ Erstellt Desktop Entry in `~/.config/autostart/`
- ✅ Fügt Anwendung zum Anwendungsmenü hinzu
- ✅ Macht alle Scripts ausführbar
- ✅ Startet automatisch bei jedem Login

#### **Autostart deaktivieren:**
```bash
# Autostart vollständig entfernen
./uninstall-autostart.sh

# Oder nur temporär deaktivieren
rm ~/.config/autostart/dirty-git-finder.desktop
```

---

## 🔄 Programmablauf - Detailliert

### **1️⃣ Anwendungsstart**

#### **1.1 Initialisierung (0-100ms)**
```
┌─────────────────────────────────────────────────┐
│ run.py oder dirty_git_finder.py wird ausgeführt │
└─────────────────────────────────────────────────┘
                    ↓
        ┌───────────────────────┐
        │ Python Import-Phase   │
        │ - tkinter             │
        │ - subprocess          │
        │ - threading           │
        │ - pathlib             │
        └───────────────────────┘
                    ↓
        ┌───────────────────────┐
        │ Hauptfenster erstellen│
        │ (Tk root window)      │
        └───────────────────────┘
```

**Was passiert:**
- Python lädt alle benötigten Module
- Tkinter-Hauptfenster wird initialisiert (1000x700 px)
- `DirtyGitFinderGUI` Klasse wird instanziiert
- Window-Icon wird gesetzt (falls vorhanden)

#### **1.2 UI-Aufbau (100-300ms)**
```
┌──────────────────────────────────────┐
│ setup_ui() wird aufgerufen           │
└──────────────────────────────────────┘
            ↓
┌──────────────────────────────────────┐
│ GUI-Komponenten erstellen:           │
│ 1. Scan-Path Eingabefeld             │
│ 2. Control Buttons (Start/Cancel)    │
│ 3. Progress Bar                      │
│ 4. Treeview (Ergebnistabelle)       │
│ 5. Filter-Optionen                   │
│ 6. Status Bar                        │
│ 7. Menüleiste                        │
│ 8. Kontextmenü                       │
└──────────────────────────────────────┘
            ↓
┌──────────────────────────────────────┐
│ Event Bindings registrieren:         │
│ - Doppelklick → Ordner öffnen        │
│ - Rechtsklick → Kontextmenü          │
│ - Einzelklick → Git-Info anzeigen    │
│ - Column-Header → Sortierung         │
└──────────────────────────────────────┘
            ↓
┌──────────────────────────────────────┐
│ Autostart-Status prüfen              │
│ check_autostart_status()             │
└──────────────────────────────────────┘
```

**Wichtige Komponenten:**
- **Treeview**: 8 Spalten (Name, Path, Branch, Status, Changes, Last Modified, Last Commit, Time Diff)
- **Filter**: Radio-Buttons (All, Dirty Only, Clean Only)
- **Autostart-Checkbox**: Zeigt aktuellen Autostart-Status

#### **1.3 Auto-Scan Start (300-500ms)**
```
┌──────────────────────────────────────┐
│ root.after(100, auto_start_scan)     │
└──────────────────────────────────────┘
            ↓
┌──────────────────────────────────────┐
│ Home-Verzeichnis als Scan-Pfad setzen│
│ path_var.set(Path.home())            │
└──────────────────────────────────────┘
            ↓
┌──────────────────────────────────────┐
│ root.after(200, start_scan)          │
└──────────────────────────────────────┘
```

**Timing:**
- 100ms Verzögerung für UI-Rendering
- 200ms weitere Verzögerung für vollständige UI-Initialisierung
- **Total: ~300ms bis Scan-Start**

---

### **2️⃣ Scan-Prozess**

#### **2.1 Scan-Initialisierung**
```
┌──────────────────────────────────────┐
│ start_scan() wird aufgerufen         │
└──────────────────────────────────────┘
            ↓
┌──────────────────────────────────────┐
│ Validierung:                         │
│ - Pfad existiert?                    │
│ - Lesezugriff vorhanden?             │
└──────────────────────────────────────┘
            ↓
┌──────────────────────────────────────┐
│ UI-Updates:                          │
│ - found_repos.clear()                │
│ - Scan-Button deaktivieren           │
│ - Cancel-Button aktivieren           │
│ - Progress: "Scanning..."            │
└──────────────────────────────────────┘
            ↓
┌──────────────────────────────────────┐
│ Worker-Thread starten                │
│ threading.Thread(_scan_worker)       │
└──────────────────────────────────────┘
```

#### **2.2 Worker-Thread Ausführung**
```
┌────────────────────────────────────────────┐
│ _scan_worker(scan_path) läuft in Thread   │
└────────────────────────────────────────────┘
            ↓
┌────────────────────────────────────────────┐
│ Callbacks definieren:                      │
│ - progress_callback(current_path)          │
│   → Updates Progress-Label                 │
│ - result_callback(repo_info)               │
│   → Fügt Repo zur Liste hinzu              │
│   → Aktualisiert Treeview                  │
└────────────────────────────────────────────┘
            ↓
┌────────────────────────────────────────────┐
│ scanner.scan_directory() aufrufen          │
│ (GitRepoScanner Instanz)                   │
└────────────────────────────────────────────┘
```

#### **2.3 Repository-Scan-Logik**
```
┌─────────────────────────────────────────────┐
│ FÜR JEDES Verzeichnis im Scan-Pfad:        │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ os.walk(start_path)                         │
│ Durchläuft rekursiv alle Unterverzeichnisse│
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Filter anwenden:                            │
│ - Überspringe versteckte Ordner            │
│   (außer .git)                              │
│ - Überspringe: node_modules, __pycache__,  │
│   .venv, venv, etc.                         │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ is_git_repo(root) prüfen                    │
│ → .git Verzeichnis vorhanden?               │
└─────────────────────────────────────────────┘
            ↓ (Ja)
┌─────────────────────────────────────────────┐
│ Repository gefunden!                        │
│ get_repo_status(root) aufrufen              │
└─────────────────────────────────────────────┘
```

#### **2.4 Git-Status-Analyse**
```
┌─────────────────────────────────────────────┐
│ get_repo_status(repo_path)                  │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Git-Befehle ausführen:                      │
│                                             │
│ 1. git branch --show-current                │
│    → Aktuellen Branch ermitteln             │
│    → Timeout: 5 Sekunden                    │
│                                             │
│ 2. git status --porcelain                   │
│    → Uncommitted Changes finden             │
│    → Timeout: 5 Sekunden                    │
│                                             │
│ 3. git log -1 --format=%ct                  │
│    → Letzten Commit-Timestamp               │
│    → Timeout: 5 Sekunden                    │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Status-Analyse:                             │
│ - Changes parsen (M, A, D, ??, etc.)        │
│ - Anzahl der Änderungen zählen              │
│ - Remote-Check (git remote)                 │
│ - Unpushed-Check (git rev-list @{u}..HEAD) │
│ - Dirty-Kriterien sammeln:                  │
│   * has_uncommitted (Changes vorhanden)     │
│   * has_remote (Remote konfiguriert)        │
│   * has_unpushed (Commits nicht gepusht)    │
│ - GUI entscheidet basierend auf Checkboxen │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Dateimetadaten sammeln:                     │
│ - get_oldest_dirty_file_time()              │
│   → Älteste modifizierte Datei finden       │
│   → Modification-Time auslesen              │
│   → Relativen Zeitstempel formatieren       │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Zeitdifferenz berechnen:                    │
│ - calculate_time_diff()                     │
│   → Commit-Zeit vs. Modifikations-Zeit      │
│   → Ausgabe: "2d alt", "5h alt", etc.       │
└─────────────────────────────────────────────┘
```

**Git-Status-Codes erklärt:**
```
M  = Modified (Datei wurde geändert)
A  = Added (Datei zum Staging hinzugefügt)
D  = Deleted (Datei gelöscht)
?? = Untracked (Datei nicht im Git-Index)
R  = Renamed (Datei umbenannt)
C  = Copied (Datei kopiert)
```

#### **2.5 Ergebnis-Verarbeitung**
```
┌─────────────────────────────────────────────┐
│ result_callback(repo_info) wird aufgerufen  │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ repo_info Dictionary enthält:               │
│ {                                           │
│   'path': '/home/user/project',             │
│   'name': 'project',                        │
│   'branch': 'main',                         │
│   'has_uncommitted': True/False,            │
│   'has_remote': True/False,                 │
│   'has_unpushed': True/False,               │
│   'changes_count': 3,                       │
│   'changes': ['M file.py', '?? new.txt'],   │
│   'oldest_modification': {                  │
│     'display': 'config.py (vor 2 Std.)',    │
│     'timestamp': 1234567890                 │
│   },                                        │
│   'last_commit': {                          │
│     'display': 'vor 1 Tag',                 │
│     'timestamp': 1234560000                 │
│   }                                         │
│ }                                           │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ found_repos.append(repo_info)               │
│ → Speichert Repo in interner Liste          │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ root.after(0, _add_repo_to_tree)            │
│ → Thread-sichere UI-Aktualisierung          │
└─────────────────────────────────────────────┘
```

#### **2.6 UI-Update (Treeview)**
```
┌─────────────────────────────────────────────┐
│ _add_repo_to_tree(repo_info)                │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Status-Emoji bestimmen:                     │
│ - DIRTY → 🔥 DIRTY (rot)                    │
│ - CLEAN → ✅ CLEAN (grün)                   │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Branch-Highlighting:                        │
│ - main/master → Standard-Farbe              │
│ - andere Branches → Rot hervorgehoben       │
│   (non_main_branch Tag)                     │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Insertion-Position:                         │
│ - DIRTY Repos → Position 0 (oben)           │
│ - CLEAN Repos → Position 'end' (unten)      │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ tree.insert() mit 8 Spalten:                │
│ [Name, Path, Branch, Status, Changes,       │
│  Last Modified, Last Commit, Time Diff]     │
└─────────────────────────────────────────────┘
```

#### **2.7 Scan-Abschluss**
```
┌─────────────────────────────────────────────┐
│ Alle Verzeichnisse durchsucht               │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ root.after(0, _scan_completed)              │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ _scan_completed() aktualisiert:             │
│ - Scan-Button aktivieren                    │
│ - Cancel-Button deaktivieren                │
│ - Progress: "Scan completed - Found X repos"│
│ - Status: "Total: X, Dirty: Y, Clean: Z"    │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ apply_filter()                              │
│ → Standard-Filter: "Dirty Only" anwenden    │
└─────────────────────────────────────────────┘
```

---

### **3️⃣ Benutzer-Interaktionen**

#### **3.1 Doppelklick auf Repository**
```
┌─────────────────────────────────────────────┐
│ User macht Doppelklick auf Tree-Item        │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ on_double_click(event) wird aufgerufen      │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ tree.selection() → Item-ID ermitteln        │
│ tree.item(item, 'values') → Pfad auslesen   │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ open_folder_in_file_manager(path)           │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Plattform-spezifischer Befehl:              │
│ - Linux: xdg-open <path>                    │
│ - macOS: open <path>                        │
│ - Windows: explorer <path>                  │
└─────────────────────────────────────────────┘
```

#### **3.2 Rechtsklick → Kontextmenü**
```
┌─────────────────────────────────────────────┐
│ User macht Rechtsklick auf Tree-Item        │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ on_right_click(event)                       │
│ - Item unter Cursor identifizieren          │
│ - Item selektieren                          │
│ - Kontextmenü an Mausposition anzeigen      │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Kontextmenü-Optionen:                       │
│                                             │
│ 📊 Git Graph anzeigen                       │
│    → show_git_graph()                       │
│    → Neues Fenster mit git log --graph      │
│                                             │
│ 🔄 Push & Pull ausführen                    │
│    → git_push_pull()                        │
│    → git pull && git push                   │
│    → Output in scrollbarem Fenster          │
│                                             │
│ 🌐 Remote URL in Browser öffnen             │
│    → git remote get-url origin              │
│    → SSH zu HTTPS konvertieren              │
│    → webbrowser.open(url)                   │
│                                             │
│ 📁 Im Datei-Explorer öffnen                 │
│    → open_in_file_browser()                 │
│                                             │
│ 💻 In VS Code öffnen                        │
│    → subprocess: code <path>                │
│                                             │
│ 🖥️ Terminal öffnen                          │
│    → Plattform-spezifischer Terminal-Start  │
└─────────────────────────────────────────────┘
```

#### **3.3 Spalten-Sortierung**
```
┌─────────────────────────────────────────────┐
│ User klickt auf Column-Header               │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ sort_treeview(column, sort_type)            │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Sortierlogik:                               │
│ - Gleiche Spalte? → Reihenfolge umkehren    │
│ - Neue Spalte? → Aufsteigend sortieren      │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Sort-Type Handling:                         │
│                                             │
│ 'alpha': Alphabetisch                       │
│   → str.lower() für Case-Insensitive        │
│                                             │
│ 'date': Nach Zeitstempel                    │
│   → _extract_date_timestamp()               │
│   → Parst "vor X Min.", "heute HH:MM", etc. │
│                                             │
│ 'timediff': Nach Zeitdifferenz              │
│   → _extract_timediff_value()               │
│   → Konvertiert "2d alt" → Minuten          │
│                                             │
│ 'numeric': Numerisch                        │
│   → _extract_numeric()                      │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Items neu anordnen:                         │
│ - tree.move(item, '', index)                │
│ - Column-Header mit Pfeil markieren         │
│   (↑ aufsteigend, ↓ absteigend)             │
└─────────────────────────────────────────────┘
```

#### **3.4 Filter ändern**
```
┌─────────────────────────────────────────────┐
│ User ändert Filter (All/Dirty/Clean)        │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ apply_filter() wird aufgerufen              │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Treeview leeren: clear_results()            │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Repositories sortieren:                     │
│ - DIRTY zuerst (sort_key = 0)               │
│ - CLEAN danach (sort_key = 1)               │
│ - Innerhalb Gruppe: Nach ältestem Timestamp │
│ - Tertiär: Alphabetisch nach Name           │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Gefilterte Repos hinzufügen:                │
│ - "all": Alle Repos                         │
│ - "dirty": Nur dirty Repos                  │
│ - "clean": Nur clean Repos                  │
└─────────────────────────────────────────────┘
```

---

### **4️⃣ Feature/Bug-Reporting**

```
┌─────────────────────────────────────────────┐
│ User klickt "Feature/Bug" Button            │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ report_feature_bug()                        │
│ - Neues Modal-Fenster (Toplevel)            │
│ - Zentriert über Hauptfenster               │
│ - Input-Feld für Beschreibung               │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ User gibt Text ein und drückt Enter         │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Text wird an feature_bugs.txt angehängt     │
│ - Projektverzeichnis ermitteln              │
│ - Datei im Append-Modus öffnen              │
│ - Zeile + Newline schreiben                 │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Bestätigung in Status-Bar anzeigen          │
└─────────────────────────────────────────────┘
```

---

### **5️⃣ Autostart-Management**

```
┌─────────────────────────────────────────────┐
│ User klickt Autostart-Checkbox              │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ toggle_autostart()                          │
│ - Plattform erkennen                        │
│ - Script-Pfad ermitteln                     │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ LINUX:                                      │
│ - ~/.config/autostart/ erstellen            │
│ - dirty-git-finder.desktop schreiben        │
│ - Datei ausführbar machen (chmod 755)       │
│                                             │
│ MACOS:                                      │
│ - ~/Library/LaunchAgents/ erstellen         │
│ - com.dirtygitfinder.plist schreiben        │
│                                             │
│ WINDOWS:                                    │
│ - Registry-Key öffnen                       │
│ - HKCU\...\Run\DirtyGitFinder setzen        │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│ Erfolgs-/Fehler-Messagebox anzeigen         │
└─────────────────────────────────────────────┘
```

---

## 🏗️ Architektur & Datenfluss

### **Architektur-Übersicht**

```
┌────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         DirtyGitFinderGUI (dirty_git_finder.py)      │  │
│  │  - Tkinter UI Management                             │  │
│  │  - Event Handling                                    │  │
│  │  - User Interactions                                 │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────┘
                           ↕
┌────────────────────────────────────────────────────────────┐
│                    BUSINESS LOGIC LAYER                     │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         GitRepoScanner (dirty_git_finder.py)         │  │
│  │  - Directory Scanning                                │  │
│  │  - Git Status Analysis                               │  │
│  │  - Time Calculations                                 │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         GitScanner (git_scanner.py)                  │  │
│  │  - Alternative Scanner Implementation                │  │
│  │  - Repository Detection                              │  │
│  │  - Change Categorization                             │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────┘
                           ↕
┌────────────────────────────────────────────────────────────┐
│                    SYSTEM LAYER                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Git CLI (subprocess)                                │  │
│  │  - git status --porcelain                            │  │
│  │  - git branch --show-current                         │  │
│  │  - git log -1 --format=%ct                           │  │
│  │  - git remote get-url origin                         │  │
│  │  - git log --graph                                   │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  File System (os, pathlib)                           │  │
│  │  - os.walk() für rekursive Suche                     │  │
│  │  - os.path.getmtime() für Timestamps                 │  │
│  │  - os.listdir() für Verzeichnisinhalte               │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────┘
```

### **Threading-Modell**

```
┌─────────────────────────────────────────────────────────────┐
│                        MAIN THREAD                           │
│  - Tkinter Event Loop (root.mainloop())                     │
│  - UI Rendering                                             │
│  - Event Handling                                           │
└─────────────────────────────────────────────────────────────┘
                           ↕ (thread-safe)
┌─────────────────────────────────────────────────────────────┐
│                       WORKER THREAD                          │
│  - _scan_worker()                                           │
│  - scanner.scan_directory()                                 │
│  - Git-Befehle ausführen                                    │
│  - Dateisystem durchsuchen                                  │
│                                                             │
│  Kommunikation mit Main Thread:                             │
│  → root.after(0, callback)  [Thread-safe UI updates]        │
└─────────────────────────────────────────────────────────────┘
```

**Thread-Sicherheit:**
- Worker-Thread führt blockierende Operationen aus
- UI-Updates IMMER über `root.after(0, callback)`
- Verhindert GUI-Freezing während langer Scans

### **Datenfluss-Diagramm**

```
START
  ↓
[User startet App] → [GUI wird initialisiert]
  ↓
[Auto-Scan startet] → [Worker-Thread erstellt]
  ↓
[os.walk() durchsucht Filesystem]
  ↓
[Für jedes Verzeichnis:]
  ├→ [.git gefunden?] → JA → [Git-Status abrufen]
  │                           ├→ git branch --show-current
  │                           ├→ git status --porcelain
  │                           ├→ git log -1
  │                           ↓
  │                      [Status-Daten parsen]
  │                           ↓
  │                      [Zeitstempel berechnen]
  │                           ↓
  │                      [repo_info Dictionary erstellen]
  │                           ↓
  │                      [result_callback()]
  │                           ↓
  │                      [root.after(0, add_to_tree)]
  │                           ↓
  │                      [UI-Update (Treeview)]
  │
  └→ NEIN → [Weiter zum nächsten Verzeichnis]

[Scan abgeschlossen]
  ↓
[apply_filter("dirty")]
  ↓
[Dirty Repos oben sortieren]
  ↓
[Anzeige aktualisieren]
  ↓
[BEREIT für User-Interaktionen]
```

---

## 📁 Projektstruktur

```
scan-for-dirty-git-repos-gui/
│
├── 🐍 dirty_git_finder.py       # Haupt-GUI-Anwendung (1470 Zeilen)
│   ├── GitRepoScanner           # Scanner-Klasse
│   │   ├── is_git_repo()
│   │   ├── is_repo_dirty()
│   │   ├── get_repo_status()
│   │   ├── get_oldest_dirty_file_time()
│   │   ├── format_relative_time()
│   │   ├── get_last_commit_info()
│   │   ├── calculate_time_diff()
│   │   ├── scan_directory()
│   │   └── cancel_scan()
│   │
│   └── DirtyGitFinderGUI        # GUI-Hauptklasse
│       ├── __init__()           # Initialisierung
│       ├── set_app_icon()       # Icon setzen
│       ├── setup_ui()           # UI-Aufbau
│       ├── start_scan()         # Scan starten
│       ├── _scan_worker()       # Worker-Thread
│       ├── on_double_click()    # Event-Handler
│       ├── on_right_click()     # Kontextmenü
│       ├── show_git_graph()     # Git-Graph anzeigen
│       ├── git_push_pull()      # Push/Pull
│       ├── sort_treeview()      # Sortierung
│       ├── apply_filter()       # Filter anwenden
│       ├── toggle_autostart()   # Autostart-Management
│       └── ... (40+ Methoden)
│
├── 🐍 git_scanner.py            # Alternative Scanner-Implementierung (244 Zeilen)
│   ├── GitRepository            # Repository-Klasse
│   │   ├── __init__()
│   │   ├── is_git_repo
│   │   ├── get_status()
│   │   └── _analyze_changes()
│   │
│   └── GitScanner               # Scanner-Klasse
│       ├── scan()
│       ├── _scan_recursive()
│       ├── _is_git_repository()
│       ├── _is_git_worktree()
│       └── cancel()
│
├── 🐍 run.py                    # Launcher-Script
│   └── main()                   # Entry Point
│
├── 🐍 create_icon.py            # Icon-Generator
│   └── Erstellt app_icon*.png
│
├── 🖼️  app_icon.png              # Anwendungs-Icons
├── 🖼️  app_icon_16.png
├── 🖼️  app_icon_32.png
├── 🖼️  app_icon_64.png
├── 🖼️  app_icon_128.png
│
├── 🔧 launch.sh                 # Shell-Launcher für Autostart
├── 🔧 autostart-install.sh      # Autostart-Installation
├── 🔧 uninstall-autostart.sh    # Autostart-Deinstallation
│
├── 🗂️  dirty-git-finder.desktop  # Linux Desktop Entry
├── 📝 feature_bugs.txt          # User-Feedback-Sammlung
├── 📖 README.md                 # Diese Datei
├── 📖 AUTOSTART-GUIDE.md        # Autostart-Dokumentation
│
└── 📁 .github/
    └── copilot-instructions.md  # Entwicklungsrichtlinien
```

---

## 📖 Bedienungsanleitung

### **Grundlegende Nutzung**

1. **Anwendung starten:**
   ```bash
   python3 dirty_git_finder.py
   ```

2. **Automatischer Scan:**
   - Startet automatisch nach ~300ms
   - Durchsucht Home-Verzeichnis rekursiv
   - Zeigt Fortschritt in Progress-Bar

3. **Ergebnisse betrachten:**
   - **DIRTY Repos**: Oben in der Liste, 🔥 Symbol
   - **CLEAN Repos**: Unten in der Liste, ✅ Symbol
   - **Non-Main-Branches**: Rot hervorgehoben

### **GUI-Komponenten**

#### **Hauptfenster**
- **Scan Path**: Eingabefeld für zu durchsuchenden Pfad
- **Browse**: Button zum Auswählen eines Verzeichnisses
- **Start Scan**: Startet neue Suche
- **Cancel**: Bricht aktuellen Scan ab
- **Clear Results**: Löscht Ergebnisliste
- **Feature/Bug**: Feedback-Dialog öffnen

#### **Filter & Optionen**
- **Show**: Radio-Buttons (All / Dirty Only / Clean Only)
- **Mark as dirty**: Checkboxen zur Auswahl der Dirty-Kriterien
  - ☑ Uncommitted changes
  - ☑ No remote
  - ☐ Unpushed commits
- **Beim Systemstart ausführen**: Autostart-Checkbox

#### **Ergebnistabelle (8 Spalten)**
1. **Repository Name**: Projektname (Verzeichnisname)
2. **Path**: Vollständiger Pfad
3. **Branch**: Aktueller Git-Branch
4. **Status**: 🔥 DIRTY oder ✅ CLEAN
5. **Changes**: Git-Status-Zeilen (M, A, D, ??) + Warnungen (⚠️ NO REMOTE, ⚠️ UNPUSHED)
6. **Älteste Änderung**: Dateiname + Zeitstempel
7. **Letzter Commit**: Wann war der letzte Commit
8. **Zeitdifferenz**: Alter der uncommitted changes

#### **Filter-Optionen**
- **All**: Zeigt alle gefundenen Repositories
- **Dirty Only**: Nur Repositories die den aktivierten Dirty-Kriterien entsprechen (Standard)
- **Clean Only**: Nur saubere Repositories

#### **Dirty-Kriterien (Einstellbar via Checkboxen)**
- **☑ Uncommitted changes** (Standard: AN): Modified, added, deleted, untracked files
- **☑ No remote** (Standard: AN): Repository hat kein Remote (GitHub/GitLab) konfiguriert
- **☐ Unpushed commits** (Standard: AUS): Commits die noch nicht auf Remote gepusht wurden

Ein Repository wird als DIRTY markiert, wenn **mindestens eines** der aktivierten Kriterien zutrifft.

### **Maus-Interaktionen**

#### **Einfacher Klick:**
- **Auf Repository**: Zeigt letzten Commit in Status-Bar
- **Auf Spalten-Header**: Sortiert nach Spalte (↑/↓)

#### **Doppelklick:**
- **Auf Repository**: Öffnet Ordner im Dateimanager
  - Linux: `xdg-open`
  - macOS: `open`
  - Windows: `explorer`

#### **Rechtsklick (Kontextmenü):**
- **📊 Git Graph anzeigen**: Commit-History in neuem Fenster
- **🔄 Push & Pull ausführen**: Git sync mit Output-Fenster
- **🌐 Remote URL in Browser**: GitHub/GitLab Seite öffnen
- **📁 Im Datei-Explorer öffnen**: System-Dateimanager
- **💻 In VS Code öffnen**: Projekt in VS Code laden
- **🖥️ Terminal öffnen**: Terminal im Projekt-Verzeichnis

### **Menüleiste**

#### **Datei-Menü:**
- 🔍 **Scan starten**: Neuen Scan beginnen
- ⏹️ **Scan abbrechen**: Laufenden Scan stoppen
- 🗑️ **Ergebnisse löschen**: Tabelle leeren
- 📝 **Feature/Bug melden**: Feedback-Dialog
- 🔧 **Open *this* Project**: Dieses Tool selbst in VS Code öffnen
- ❌ **Beenden**: Anwendung schließen

### **Tastatur-Shortcuts**

- **Escape**: Kontextmenü schließen
- **Pfeiltasten**: Navigation in Repository-Liste
- **Enter**: Gewähltes Repository im Dateimanager öffnen

### **Dirty-Kriterien anpassen**

Du kannst selbst bestimmen, welche Bedingungen ein Repository als "dirty" markieren:

1. **Standardeinstellung (Entwickler-Workflow):**
   - ☑ Uncommitted changes (lokale Änderungen)
   - ☑ No remote (kein Backup auf GitHub/GitLab)
   - ☐ Unpushed commits (aus)

2. **Release-Manager-Workflow:**
   - ☐ Uncommitted changes (aus)
   - ☐ No remote (aus)
   - ☑ Unpushed commits (zeigt nur Repos mit unpushed commits)

3. **Backup-Check:**
   - ☐ Uncommitted changes (aus)
   - ☑ No remote (zeigt nur Repos ohne Remote-Backup)
   - ☐ Unpushed commits (aus)

**Hinweis:** Die Anzeige wird sofort aktualisiert, wenn du eine Checkbox änderst.

---

## 🔧 Troubleshooting

### **Häufige Probleme**

#### **1. "Git nicht gefunden" Fehler**
```bash
# Git installieren (Ubuntu/Debian)
sudo apt install git

# Git installieren (macOS)
brew install git

# Git installieren (Windows)
# Herunterladen von: https://git-scm.com
```

**Prüfen:**
```bash
git --version  # Sollte Version anzeigen
which git      # Sollte Pfad zu Git anzeigen
```

#### **2. Tkinter nicht verfügbar**
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# Fedora/CentOS
sudo yum install tkinter

# macOS (mit Homebrew)
brew install python-tk
```

**Testen:**
```python
python3 -c "import tkinter; print('Tkinter OK')"
```

#### **3. Berechtigungsfehler beim Scan**
```
PermissionError: [Errno 13] Permission denied
```

**Lösung:**
- Wählen Sie einen anderen Scan-Pfad
- Überprüfen Sie Leserechte: `ls -la /pfad`
- Vermeiden Sie System-Verzeichnisse (/root, /sys, /proc)

#### **4. Langsame Scans**
**Ursachen:**
- Großes Home-Verzeichnis mit vielen Dateien
- Netzwerk-Laufwerke im Scan-Pfad
- Viele große Repositories

**Optimierungen:**
- Wählen Sie spezifischeren Pfad (z.B. ~/Projekte statt ~)
- Ausschluss großer Verzeichnisse wird automatisch gemacht
- Reduzieren Sie max_depth (im Code anpassbar)

#### **5. Icon wird nicht angezeigt**
**Lösung:**
```bash
# PIL installieren (falls noch nicht vorhanden)
pip3 install pillow

# Icon manuell generieren
python3 create_icon.py
```

#### **6. Autostart funktioniert nicht**

**Linux:**
```bash
# Prüfen ob Desktop Entry existiert
ls -la ~/.config/autostart/dirty-git-finder.desktop

# Prüfen ob Datei ausführbar ist
chmod +x ~/.config/autostart/dirty-git-finder.desktop

# Manuell testen
python3 /pfad/zu/dirty_git_finder.py
```

**macOS:**
```bash
# LaunchAgent prüfen
ls -la ~/Library/LaunchAgents/com.dirtygitfinder.plist

# Laden
launchctl load ~/Library/LaunchAgents/com.dirtygitfinder.plist
```

**Windows:**
```powershell
# Registry-Key prüfen
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v DirtyGitFinder
```

### **Debug-Modus**

Für detailliertes Debugging aktivieren Sie Logging:

```python
# Am Anfang von dirty_git_finder.py hinzufügen:
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

---

## 🛠️ Entwicklung & Anpassungen

### **Ausgeschlossene Verzeichnisse erweitern**

In `dirty_git_finder.py`, Zeile 249:
```python
# Skip common non-repository directories
dirs[:] = [d for d in dirs if not d.startswith('.') or d == '.git']
```

Oder in `git_scanner.py`, Zeile 113:
```python
self.excluded_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', 'build', 'dist'}
```

### **Scan-Tiefe begrenzen**

In `git_scanner.py`, Zeile 120:
```python
repositories = self._scan_recursive(
    root_path,
    repositories,
    progress_callback,
    repo_found_callback,
    current_depth=0,
    max_depth=5  # Hier anpassen!
)
```

### **Git-Timeout anpassen**

In `dirty_git_finder.py`, Zeilen 37, 54, 64, 176:
```python
subprocess.run(
    ['git', 'status', '--porcelain'],
    cwd=repo_path,
    capture_output=True,
    text=True,
    timeout=10  # Von 5 auf 10 Sekunden erhöhen
)
```

### **Standard-Filter ändern**

In `dirty_git_finder.py`, Zeile 485:
```python
self.filter_var = tk.StringVar(value="all")  # Statt "dirty"
```

### **Fenstergröße anpassen**

In `dirty_git_finder.py`, Zeile 281:
```python
self.root.geometry("1200x800")  # Statt 1000x700
```

### **Spaltenbreiten ändern**

In `dirty_git_finder.py`, Zeilen 403-410:
```python
self.tree.column('Name', width=150)  # Breiter machen
self.tree.column('Path', width=200)
# etc.
```

---

## 📊 Performance-Metriken

### **Typische Scan-Zeiten**

| Verzeichnisgröße | Anzahl Repos | Scan-Zeit | RAM-Nutzung |
|------------------|--------------|-----------|-------------|
| ~/Dokumente      | 5-10         | 5-15s     | 50 MB       |
| ~/ (Home)        | 20-50        | 30-120s   | 80 MB       |
| /home/users/     | 100+         | 2-5 min   | 150 MB      |

**Abhängig von:**
- Anzahl Verzeichnisse
- Festplattengeschwindigkeit (SSD vs. HDD)
- Anzahl Git-Repositories
- Netzwerk-Laufwerke (sehr langsam!)

---

## 📜 Lizenz

Dieses Projekt steht unter der MIT-Lizenz.

---

## 🤝 Beitragen

1. Fork des Repositories erstellen
2. Feature-Branch erstellen (`git checkout -b feature/amazing-feature`)
3. Änderungen committen (`git commit -m 'Add amazing feature'`)
4. Branch pushen (`git push origin feature/amazing-feature`)
5. Pull Request erstellen

---

## 📝 Changelog

### v2.1.0 (2026-02-12)
- **Einstellbare Dirty-Kriterien**: Checkboxen zur Auswahl was als "dirty" gilt
- **Uncommitted changes**: Standard-Kriterium (an)
- **No remote**: Repository ohne Remote-Backup (an)
- **Unpushed commits**: Commits die nicht gepusht wurden (aus, aktivierbar)
- **Dynamische Aktualisierung**: Sofortige Neuberechnung bei Checkbox-Änderung
- **Erweiterte Anzeige**: ⚠️ UNPUSHED zusätzlich zu ⚠️ NO REMOTE

### v2.0.0 (2026-02-12)
- Detaillierte README mit Programmablauf
- Architektur-Dokumentation
- Datenfluss-Diagramme
- Projektstruktur reorganisiert (src/, scripts/, assets/, docs/, config/)
- Remote-Check: Repos ohne Remote werden als dirty markiert

### v1.1.0
- Autostart-Support für Linux-Desktops
- Automatische Installations- und Deinstallationsskripte
- Desktop Entry Integration
- Launch-Script für zuverlässigen Start

### v1.0.0
- Initiale Veröffentlichung
- GUI mit tkinter
- Rekursive Git-Repository-Suche
- Status-Überprüfung für dirty/clean Repositories
- Filter- und Sortieroptionen
- Multi-Threading-Unterstützung

---

## ⚠️ Bekannte Einschränkungen

- Sehr große Verzeichnisstrukturen (>100.000 Dateien) können lange Scan-Zeiten verursachen
- Git-Repositories in symbolisch verlinkten Verzeichnissen werden möglicherweise nicht erkannt
- Windows-Pfade mit Umlauten könnten Probleme verursachen
- Scan kann nicht pausiert werden (nur Abbruch möglich)
- Keine parallele Scan-Threads (ein Thread pro Scan)

---

## 💡 Support

Bei Problemen oder Fragen:
- **Feature/Bug melden**: Nutzen Sie den integrierten Feature/Bug-Button in der App
- **GitHub Issues**: Erstellen Sie ein Issue im Repository
- **Email**: Kontaktieren Sie den Entwickler

---

**Hinweis**: Diese Anwendung führt nur lesende Git-Operationen aus und nimmt keine Änderungen an Ihren Repositories vor (außer bei expliziter Nutzung von Push/Pull).
