<img width="60%"  alt="image" src="https://github.com/user-attachments/assets/f03b10ca-8587-4edd-a660-8c6a340457f0" />


# 🔥 Dirty Git Repository Finder GUI

Eine professionelle Python GUI-Anwendung, die Ihr System nach Git-Repositories durchsucht und detailliert anzeigt, welche davon "dirty" sind (uncommitted changes haben). Perfekt für Entwickler, die einen schnellen Überblick über den Status ihrer Projekte benötigen.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)

---

## 📋 Inhaltsverzeichnis {#toc}

1. [Features](#features)
2. [Systemvoraussetzungen](#requirements)
3. [Installation & Setup](#installation)
4. [Makefile & Build-System](#makefile-build)
5. [Programmablauf - Detailliert](#workflow)
6. [Architektur & Datenfluss](#architecture)
7. [Projektstruktur](#structure)
8. [Bedienungsanleitung](#usage)
9. [Troubleshooting](#troubleshooting)
10. [Entwicklung & Anpassungen](#development)

---

## ⭐ Features {#features}

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

## 📋 Systemvoraussetzungen {#requirements}

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

## 🚀 Installation & Setup {#installation}

### **Methode 1: pip/pipx (Empfohlen)**

```bash
# Mit pip installieren
pip install dirty-git-finder

# Oder mit pipx (isolierte Umgebung)
pipx install dirty-git-finder

# Starten
dirty-git-finder
```

### **Methode 2: Git Clone + Make**

```bash
# Repository klonen
git clone https://github.com/dajuly20/scan-for-dirty-git-repos-gui.git
cd scan-for-dirty-git-repos-gui

# Für aktuellen Benutzer installieren
make install-user

# Oder system-weit (benötigt sudo)
make install

# Starten
dirty-git-finder
```

### **Methode 3: Entwicklermodus**

```bash
git clone https://github.com/dajuly20/scan-for-dirty-git-repos-gui.git
cd scan-for-dirty-git-repos-gui

# Im Entwicklermodus installieren (editierbar)
make install-dev

# Oder direkt starten ohne Installation
make run
# oder: python3 run.py
```

### **Methode 4: Direkter Download**

1. **Dateien herunterladen:**
   - Laden Sie das Repository als ZIP herunter
   - Entpacken Sie es in einen Ordner

2. **Starten:**
   ```bash
   cd scan-for-dirty-git-repos-gui
   python3 run.py
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

## � Makefile & Build-System

Das Projekt verwendet ein **Makefile** zur Automatisierung häufiger Entwicklungs- und Build-Aufgaben. Dies stellt sicher, dass alle Befehle konsistent und korrekt ausgeführt werden.

### **Makefile-Struktur & Überblick**

Das Makefile befindet sich im Projektroot und enthält etwa 15+ Ziele (Targets) für verschiedene Aufgaben. Es nutzt Python 3.12 mit einer **Virtual Environment (.venv)** zur Isolation aller Dependencies.

**Wichtiger Hinweis:** Das Makefile ist so konfiguriert, dass es die Python-Interpreter und Tools aus der `.venv/` verwendet, nicht aus dem System. Dies garantiert:
- ✅ Konsistente Abhängigkeitsversionen
- ✅ Keine Konflikte mit System-Python
- ✅ Reproducible Builds auf verschiedenen Systemen

### **Vollständige Befehlsreferenz**

#### **🏠 Hilfe & Überblick**
```bash
make help          # Zeigt alle verfügbaren Befehle mit Beschreibungen
```

#### **📦 Installation (verschiedene Modi)**
```bash
# System-weit installieren (erfordert sudo/Admin-Rechte)
make install

# Für aktuellen Benutzer (~/.local/bin wird verwendet)
make install-user

# Entwicklermodus (editable install - Änderungen sofort wirksam)
make install-dev

# Deinstallieren
make uninstall
```

#### **▶️ Anwendung ausführen**
```bash
# Startet die GUI-Anwendung direkt
make run

# Entspricht: .venv/bin/python run.py
```

#### **🏗️ Paket bauen**
```bash
# Erstellt BEIDE: Wheel (.whl) + Source Distribution (.tar.gz)
make build

# Nur Wheel (schneller, für lokale Installation)
make wheel

# Nur Source Distribution (für PyPI)
make sdist

# Beispiel: dist/ enthält dann:
# ├── dirty_git_finder-2.2.0-py3-none-any.whl
# └── dirty_git_finder-2.2.0.tar.gz
```

##### **📦 Was ist ein Wheel (.whl)?**

Ein **Wheel** ist ein vorkompiliertes, installationsfertiges Python-Paketformat:

| Aspekt | Wheel (.whl) | Source (.tar.gz) |
|--------|---------|----------|
| **Format** | Binary, vorkompiliert | Quellcode |
| **Installation** | ⚡ Schnell (1-2 Sek.) | 🐢 Langsam (Compilation) |
| **Größe** | Größer | Kleiner |
| **Abhängigkeiten** | Enthalten | Müssen installiert werden |
| **Verwendung** | End-User (pip install) | Entwickler, PyPI |

**Beispiel: Wheel-Dateiname erklärt**
```
dirty_git_finder-2.2.0-py3-none-any.whl
                 │      │   │    │
                 │      │   │    └─ Kompatibilität: any (alle Systeme)
                 │      │   └────── ABI: none (kein C-Code)
                 │      └────────── Python: py3 (Python 3.x)
                 └────────────────── Version: 2.2.0
```

**Praktisches Beispiel:**
```bash
# Wheel bauen (schnell!)
make wheel

# Installation aus Wheel (sehr schnell!)
pip install dist/dirty_git_finder-2.2.0-py3-none-any.whl

# Vs. Source Distribution (muss während Installation kompilieren)
pip install dist/dirty_git_finder-2.2.0.tar.gz  # ⏳ langsamer
```

##### **💾 Installation aus Wheel vs. Tarball**

**Wheel Installation (EMPFOHLEN):**
```bash
# Paket bauen
make wheel

# Installation (schnell - nur 1-2 Sekunden!)
pip install dist/dirty_git_finder-2.2.0-py3-none-any.whl

# Oder gleich nach Build
pip install dist/*.whl

# Nach Installation testen
dirty-git-finder
```

**Tarball Installation (Quellcode):**
```bash
# Paket bauen
make sdist

# Installation (langsamer - muss kompilieren!)
pip install dist/dirty_git_finder-2.2.0.tar.gz

# Nach Installation testen
dirty-git-finder
```

**Unterschiede beim Installieren:**

| Aktion | Wheel | Tarball |
|--------|-------|---------|
| **Zeit** | ⚡ Sofort (1-2 sec) | 🐢 Langsam (5-10 sec) |
| **Was passiert** | Kopiert fertige Dateien | Dekomprimiert + kompiliert |
| **Fehlerquellen** | Keine | Compilation kann fehlschlagen |
| **Größe** | Größer (~1-2 MB) | Kleiner (~0.5 MB) |
| **Ideal für** | End-User, CI/CD | Entwickler, Quellcode-Archiv |

**Praktische Tipps:**
```bash
# Aktuelle Version auflisten
pip show dirty-git-finder

# Neu installieren (old version erst deinstallieren)
pip uninstall -y dirty-git-finder
pip install dist/dirty_git_finder-2.2.0-py3-none-any.whl

# Aus mehreren Wheels das neueste nehmen
pip install dist/*-py3-none-any.whl

# Ohne System-weit zu installieren (nur für Tests)
python -m pip install --user dist/dirty_git_finder-2.2.0-py3-none-any.whl
```

**Fazit:** Wheels sind **vorkompilierte Fertig-Pakete** — schnell, zuverlässig, ohne Compilation! 🚀

#### **🧹 Aufräumen**
```bash
# Entfernt alle Build-Artefakte
make clean

# Detailed: Löscht:
# ├── build/              # Build-Verzeichnis
# ├── dist/               # Distribution (Wheels, Tarballs)
# ├── *.egg-info/         # Egg-Info Verzeichnisse
# └── __pycache__/        # Python Cache-Dateien
```

#### **🔍 Code-Qualität**
```bash
# Führt Linting durch (pylint + flake8)
make lint

# Details:
# - pylint: Prüft Code-Stil und potenzielle Fehler
# - flake8: PEP8-Compliance und Best Practices
```

#### **✅ Tests**
```bash
# Placeholder für Tests (noch nicht implementiert)
make test

# TODO: Wird später mit pytest Tests gefüllt
```

#### **🚀 Veröffentlichung (PyPI)**
```bash
# Testet, ob Paket korrekt gebaut werden kann
make check

# Hochladen zu TestPyPI (zum Testen vor echtem Upload)
make publish-test

# Hochladen zu PyPI (öffentliche Veröffentlichung)
make publish

# Notwendig: PyPI-Token in ~/.pypirc oder als Environment-Variable
```

#### **� GitHub Releases (Binaries zum Download)**

Binaries auf GitHub als **Releases** anbieten — Benutzer können direkt von GitHub downloaden!

##### **Manuell: Release erstellen**

```bash
# 1. Paket bauen
make build

# 2. Auf GitHub gehen: github.com/dajuly20/scan-for-dirty-git-repos-gui/releases
# 3. "Create a new release"
# 4. Tag eingeben: v2.2.0
# 5. Title: Release v2.2.0
# 6. Dateien hochladen:
#    - dist/dirty_git_finder-2.2.0-py3-none-any.whl
#    - dist/dirty_git_finder-2.2.0.tar.gz
# 7. Publish

# Benutzer können dann herunterladen:
wget https://github.com/dajuly20/scan-for-dirty-git-repos-gui/releases/download/v2.2.0/dirty_git_finder-2.2.0-py3-none-any.whl
pip install dirty_git_finder-2.2.0-py3-none-any.whl
```

##### **Automatisiert: GitHub Actions Workflow**

Mit dem beiliegenden `.github/workflows/release.yml` läuft alles automatisch:

```bash
# 1. Tag erstellen und pushen
git tag v2.2.0
git push origin v2.2.0

# 2. GitHub Actions baut automatisch & lädt zu Releases hoch!
# → Fertig! Binaries sind unter "Releases" verfügbar
```

**Workflow-Details:**
- ✅ Baut automatisch Wheel + Tarball
- ✅ Lädt beide zu GitHub Releases hoch
- ✅ Sichtbar unter: github.com/dajuly20/.../releases
- ✅ Benutzer können direkt herunterladen

##### **Download-Links für Dokumentation**

In Update-Guide oder README add:
```markdown
## Installation

### Option 1: Neueste Version von GitHub
[Neueste Release herunterladen](https://github.com/dajuly20/scan-for-dirty-git-repos-gui/releases/latest)

Dann:
```bash
pip install dirty_git_finder-*.whl
```

### Option 2: pip (PyPI)
```bash
pip install dirty-git-finder
```
```

#### **�🔄 Autostart-Integration**
```bash
# Aktiviert Autostart beim Systemstart
make autostart

# Deaktiviert Autostart
make autostart-remove

# Details:
# - Linux: Erstellt ~/.config/autostart/dirty-git-finder.desktop
# - macOS: Erstellt ~/Library/LaunchAgents Eintrag
# - Windows: Registry HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
```

### **Makefile-Interna erklärt**

#### **1. Python Environment Setup**
```makefile
# Das Makefile verwendet NICHT python3 oder python direkt,
# sondern .venv/bin/python für Konsistenz:

build: clean
    .venv/bin/python -m build

run:
    .venv/bin/python run.py
```

**Warum?** Wenn `python3 -m build` ohne `.venv/` verwendet wird, sucht es im System-Python oder einer anderen Umgebung. Die Abhängigkeiten sind möglicherweise dort nicht installiert.

#### **2. .PHONY Targets**
```makefile
.PHONY: help install install-dev run build clean lint test

# Dies teilt make mit, dass diese keine echten Dateien sind,
# sondern Befehle/Targets
```

#### **3. Clean Target**
```makefile
clean:
    rm -rf build/
    rm -rf dist/
    rm -rf *.egg-info/
    find . -type d -name __pycache__ -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete
```

Dies stellt sicher, dass alte Build-Artefakte nicht zu Problemen führen.

#### **4. Build mit Dependencies**
```makefile
# 'build' hängt von 'clean' ab:
build: clean
    .venv/bin/python -m build

# Bedeutet: make build führt zuerst 'make clean' aus, dann 'make build'
```

### **Häufige Workflows**

#### **Entwicklung und Testen**
```bash
# 1. Änderungen machen im Code
# 2. Lint durchführen
make lint

# 3. Neue Features testen
make run

# 4. Lokal installieren zum Testen
make install-dev
```

#### **Für Release / Veröffentlichung**
```bash
# 1. Code überprüfen
make lint

# 2. Paket bauen
make build

# 3. Auf TestPyPI testen
make publish-test

# 4. Nach erfolgreicher Test - auf PyPI hochladen
make publish
```

#### **Cleanup vor Commit**
```bash
# Build-Artefakte entfernen
make clean

# Dann commiten
git add .
git commit -m "Your message"
```

### **Troubleshooting für Makefile-Probleme**

| Problem | Lösung |
|---------|--------|
| `make: command not found` | `sudo apt install make` (Linux) oder Homebrew (macOS) |
| `No module named build` | Virtual Env nicht aktiviert; `.venv/` existiert nicht. Lösung: `pip install build` in .venv |
| `Permission denied` | Scripts müssen executable sein: `chmod +x *.sh` |
| `.venv/bin/python: No such file` | Virtual Env fehlt. Lösung: `python3 -m venv .venv` oder `pip install -e .` |
| `ModuleNotFoundError` bei make lint | `pip install pylint flake8` in .venv |

### **Manueller Weg (ohne Makefile)**

Falls das Makefile nicht verfügbar ist (z.B. auf Windows ohne WSL):

```bash
# Virtual Environment erstellen
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# oder: .venv\Scripts\activate  # Windows

# Dependencies installieren
pip install -e ".[dev]"

# Anwendung starten
python run.py

# Paket bauen
python -m build

# Linting
pylint src/*.py
flake8 src/ --max-line-length=120
```

---
## �🔄 Programmablauf - Detailliert

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
├── 📦 pyproject.toml            # PyPI-Paketkonfiguration
├── 🔧 Makefile                  # Build-Automatisierung
├── 🐍 run.py                    # Launcher-Script (Entry Point)
│
├── 📁 src/                      # Python-Paketverzeichnis
│   ├── 🐍 __init__.py           # Paket-Initialisierung
│   │
│   ├── 🐍 dirty_git_finder.py   # Haupt-GUI-Anwendung (~1500 Zeilen)
│   │   ├── GitRepoScanner       # Scanner-Klasse
│   │   │   ├── is_git_repo()
│   │   │   ├── is_repo_dirty()
│   │   │   ├── get_repo_status()
│   │   │   ├── get_oldest_dirty_file_time()
│   │   │   ├── format_relative_time()
│   │   │   ├── get_last_commit_info()
│   │   │   ├── calculate_time_diff()
│   │   │   ├── scan_directory()
│   │   │   └── cancel_scan()
│   │   │
│   │   └── DirtyGitFinderGUI    # GUI-Hauptklasse
│   │       ├── __init__()
│   │       ├── setup_ui()
│   │       ├── start_scan()
│   │       ├── show_git_graph()
│   │       ├── git_push_pull()
│   │       ├── toggle_autostart()
│   │       └── ... (40+ Methoden)
│   │
│   └── 🐍 git_scanner.py        # Alternative Scanner-Implementierung
│       ├── GitRepository        # Repository-Klasse
│       └── GitScanner           # Scanner-Klasse
│
├── 📁 scripts/                  # Shell-Skripte
│   ├── 🔧 launch.sh             # Shell-Launcher für Autostart
│   ├── 🔧 autostart-install.sh  # Autostart-Installation (interaktiv)
│   └── 🔧 uninstall-autostart.sh # Autostart-Deinstallation
│
├── 📁 assets/                   # Ressourcen
│   ├── 🖼️  app_icon.png          # Anwendungs-Icons
│   ├── 🖼️  app_icon_16.png
│   ├── 🖼️  app_icon_32.png
│   ├── 🖼️  app_icon_64.png
│   ├── 🖼️  app_icon_128.png
│   └── 🐍 create_icon.py        # Icon-Generator
│
├── 📁 config/                   # Konfigurationsdateien
│   └── 🗂️  dirty-git-finder.desktop  # Linux Desktop Entry
│
├── 📁 docs/                     # Dokumentation
│   ├── 📖 README.md             # Diese Datei
│   └── 📖 AUTOSTART-GUIDE.md    # Autostart-Dokumentation
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

## 📦 Paket bauen & veröffentlichen

### **Voraussetzungen**

```bash
# Build-Tools installieren
pip install build twine
```

### **Makefile-Befehle**

```bash
make help           # Zeigt alle verfügbaren Befehle

# Installation
make install        # System-weit installieren (sudo erforderlich)
make install-user   # Für aktuellen Benutzer (~/.local/bin)
make install-dev    # Entwicklermodus (editierbar)
make uninstall      # Deinstallieren

# Entwicklung
make run            # Anwendung direkt starten
make lint           # Code-Linting (pylint, flake8)
make test           # Tests ausführen

# Paket bauen
make build          # Wheel und Source-Distribution erstellen
make sdist          # Nur Source-Distribution
make wheel          # Nur Wheel

# Veröffentlichen
make check          # Paket vor Upload prüfen
make publish-test   # Auf TestPyPI hochladen
make publish        # Auf PyPI hochladen

# Aufräumen
make clean          # Build-Artefakte löschen

# Autostart
make autostart          # Autostart aktivieren
make autostart-remove   # Autostart deaktivieren
```

### **Manuelles Bauen**

```bash
# Build-Verzeichnis säubern
rm -rf build/ dist/ *.egg-info/

# Paket bauen
python3 -m build

# Ergebnis prüfen
python3 -m twine check dist/*

# Auf TestPyPI testen
python3 -m twine upload --repository testpypi dist/*

# Auf PyPI veröffentlichen
python3 -m twine upload dist/*
```

### **Lokale Installation testen**

```bash
# Aus dem Build installieren
pip install dist/dirty_git_finder-*.whl

# Oder direkt vom Quellcode
pip install .

# Testen
dirty-git-finder
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

### v2.2.0 (2026-04-15)
- **PyPI-Paket**: Installation via `pip install dirty-git-finder` oder `pipx`
- **Makefile**: Build-Automatisierung mit `make install`, `make build`, `make publish`
- **Autostart-Fix**: Dynamische Pfadgenerierung statt hardcodierter Pfade
- **Interaktive Installation**: `autostart-install.sh` fragt jetzt ob Autostart aktiviert werden soll
- **Symlink-Support**: `os.path.realpath()` für korrekte Pfadauflösung bei Symlinks
- **Desktop-Entry-Fix**: Korrekte Dateirechte (0o644 statt 0o755)
- **CLI-Integration**: `dirty-git-finder` Symlink in `~/.local/bin/`
- **Verbesserte Dokumentation**: Aktualisierte Anleitungen und Copilot-Instructions

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
