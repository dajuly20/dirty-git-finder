# 🔥 Dirty Git Repository Finder GUI

Eine professionelle Python GUI-Anwendung, die Ihr System nach Git-Repositories durchsucht und detailliert anzeigt, welche davon "dirty" sind (uncommitted changes haben). Perfekt für Entwickler, die einen schnellen Überblick über den Status ihrer Projekte benötigen.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)

## 📸 Screenshots

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ Repository Name │ Path            │ Branch │ Status    │ Changes │ Älteste Änd.│
├─────────────────────────────────────────────────────────────────────────────────┤
│ ProjectAlpha    │ /home/dev/alpha │ main   │ 🔥 DIRTY  │ 3       │ config.py... │
│ ProjectBeta     │ /home/dev/beta  │ dev    │ 🔥 DIRTY  │ 1       │ main.py...   │
│ ProjectGamma    │ /home/dev/gamma │ main   │ ✅ CLEAN  │ 0       │ -            │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## ⭐ Features

### 🔍 **Intelligente Repository-Suche**
- **Rekursive Scan-Engine**: Durchsucht das gesamte Dateisystem nach Git-Repositories
- **Performance-Optimiert**: Überspringt automatisch `.git`, `node_modules`, `__pycache__` etc.
- **Anpassbare Pfade**: Startet im Home-Verzeichnis, aber jeder Pfad wählbar
- **Echtzeit-Updates**: Live-Anzeige der gefundenen Repositories während des Scans

### 🎯 **Erweiterte Git-Status-Analyse**
- **Detaillierte Dirty-Detection**: Erkennt modified, added, deleted, untracked files
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

## 🚀 Installation & Setup

### **Methode 1: Git Clone (Empfohlen für Entwickler)**

```bash
# Repository klonen
git clone https://github.com/dajuly20/BashScripts.git
cd BashScripts/finddirtygitgui

# System-Check durchführen
python3 --version  # Sollte 3.7+ anzeigen
git --version      # Git sollte verfügbar sein

# Anwendung starten
python3 dirty_git_finder.py
```

### **Methode 2: Direct Download**

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

### **Methode 3: System-Installation (Erweitert)**

```bash
# In ~/bin installieren (Linux/macOS)
mkdir -p ~/bin
cp dirty_git_finder.py ~/bin/
cp git_scanner.py ~/bin/
chmod +x ~/bin/dirty_git_finder.py

# ~/.bashrc oder ~/.zshrc ergänzen:
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc

# Alias erstellen (optional)
echo 'alias gitdirty="python3 ~/bin/dirty_git_finder.py"' >> ~/.bashrc
```

### **🚀 Autostart Installation (Empfohlen)**

Das Programm kann automatisch beim Login gestartet werden, sodass Sie immer einen Überblick über Ihre Git-Repositories haben.

#### **Automatische Installation:**
```bash
# Ins Projektverzeichnis wechseln
cd /home/julian/Documents/Goding\ Project\ Git/scan-for-dirty-git-repos-gui

# Autostart installieren
./install-autostart.sh
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

#### **Manueller Start (ohne Autostart):**
```bash
./launch.sh
# oder
python3 run.py
```

### **🔧 Desktop-Integration (Manuell)**

#### **Linux - Desktop Entry erstellen:**
```bash
cat > ~/.local/share/applications/dirty-git-finder.desktop << EOF
[Desktop Entry]
Name=Dirty Git Finder
Comment=Git Repository Status Monitor
Exec=python3 /pfad/zu/dirty_git_finder.py
Icon=git
Type=Application
Categories=Development;
Terminal=false
EOF
```

#### **macOS - Dock Integration:**
```bash
# Automator verwenden um .app zu erstellen
# oder Alias im Applications Ordner erstellen
```

#### **Windows - Verknüpfung erstellen:**
- Rechtsklick auf `dirty_git_finder.py`
- "Verknüpfung erstellen"
- Verknüpfung auf Desktop oder in Startmenü verschieben

## 📖 Detaillierte Bedienungsanleitung

### **🎯 Erste Schritte**

1. **Programm starten**: `python3 dirty_git_finder.py`
2. **Automatischer Scan**: Das Programm startet automatisch einen Scan Ihres Home-Verzeichnisses
3. **Ergebnisse betrachten**: Dirty Repositories werden rot markiert und oben angezeigt
4. **Interaktionen**: Klicken, sortieren und filtern Sie nach Belieben

### **🖱️ Maus-Interaktionen**

#### **Einfacher Klick:**
- **Auf Repository**: Zeigt letzten Commit in der Statusleiste
- **Auf Spalten-Header**: Sortiert nach dieser Spalte (aufsteigend/absteigend)

#### **Doppelklick:**
- **Auf Repository**: Öffnet Ordner im System-Dateimanager

#### **Rechtsklick:**
- **Kontextmenü mit Optionen:**
  - 📊 **Git Graph anzeigen**: Detaillierte Commit-History
  - 🌐 **Remote URL in Browser**: Öffnet GitHub/GitLab Seite
  - 📁 **Im Datei-Explorer öffnen**: System-Dateimanager
  - 💻 **In VS Code öffnen**: Projekt in Visual Studio Code

### **⌨️ Tastatur-Shortcuts**

- **Escape**: Schließt geöffnete Kontextmenüs
- **Pfeiltasten**: Navigation in der Repository-Liste
- **Enter**: Öffnet gewähltes Repository im Dateimanager
- **F5**: Startet neuen Scan (falls implementiert)

### **🔧 Erweiterte Funktionen**

### Grundlegende Nutzung

1. **Anwendung starten:**
   ```bash
   python3 dirty_git_finder.py
   ```

2. **Scan-Pfad auswählen:**
   - Standardmäßig wird das Home-Verzeichnis (~) verwendet
   - Über "Browse" kann ein anderer Pfad gewählt werden

3. **Scan starten:**
   - Klicken Sie auf "Start Scan"
   - Der Scan läuft im Hintergrund und kann jederzeit abgebrochen werden

4. **Ergebnisse betrachten:**
   - Repositories werden in einer Tabelle angezeigt
   - "Dirty" Repositories sind rot markiert
   - Filteroptionen ermöglichen die Anzeige spezifischer Repository-Typen

### GUI-Komponenten

#### Hauptfenster
- **Scan Path**: Eingabefeld für den zu durchsuchenden Pfad
- **Browse**: Button zum Auswählen eines Verzeichnisses
- **Start Scan**: Startet die Suche nach Git-Repositories
- **Cancel**: Bricht den aktuellen Scan ab
- **Clear Results**: Löscht die Ergebnisliste

#### Ergebnistabelle
- **Name**: Repository-Name (Verzeichnisname)
- **Path**: Vollständiger Pfad zum Repository
- **Branch**: Aktueller Git-Branch
- **Status**: DIRTY oder CLEAN
- **Changes**: Anzahl der uncommitted changes

#### Filter-Optionen
- **All**: Zeigt alle gefundenen Repositories
- **Dirty Only**: Zeigt nur Repositories mit uncommitted changes
- **Clean Only**: Zeigt nur saubere Repositories

### Kommandozeilen-Alternative

Für erweiterte Nutzung können Sie auch das Scanner-Modul direkt verwenden:

```python
from git_scanner import GitScanner, GitRepository

scanner = GitScanner()
repos = scanner.scan("/path/to/search")

for repo in repos:
    status = repo.get_status()
    if status['is_dirty']:
        print(f"DIRTY: {repo.path} ({status['total_changes']} changes)")
```

## Projektstruktur

```
finddirtygitgui/
├── dirty_git_finder.py         # Haupt-GUI-Anwendung
├── git_scanner.py              # Git-Repository Scanner-Modul
├── run.py                      # Launcher-Script
├── launch.sh                   # Shell-Launcher für Autostart
├── dirty-git-finder.desktop    # Desktop Entry Datei
├── install-autostart.sh        # Autostart-Installation
├── uninstall-autostart.sh      # Autostart-Deinstallation
├── README.md                   # Diese Datei
└── .github/
    └── copilot-instructions.md # Entwicklungsrichtlinien
```

## Funktionsweise

### Git-Repository-Erkennung
- Sucht nach `.git`-Verzeichnissen oder -Dateien
- Unterstützt sowohl normale Repositories als auch Git-Worktrees
- Überspringt häufige Build-/Cache-Verzeichnisse

### Status-Überprüfung
- Verwendet `git status --porcelain` für genaue Status-Information
- Kategorisiert Änderungen (modified, added, deleted, untracked)
- Timeout-Schutz für hängende Git-Operationen

### Performance-Optimierung
- Multi-Threading verhindert GUI-Blockierung
- Intelligente Verzeichnis-Filterung
- Maximale Scan-Tiefe begrenzt Ressourcenverbrauch

## Troubleshooting

### Häufige Probleme

1. **"Git nicht gefunden" Fehler:**
   ```bash
   # Git installieren (Ubuntu/Debian)
   sudo apt install git
   
   # Git installieren (macOS)
   brew install git
   ```

2. **Tkinter nicht verfügbar:**
   ```bash
   # Ubuntu/Debian
   sudo apt install python3-tk
   
   # Fedora/CentOS
   sudo yum install tkinter
   ```

3. **Berechtigungsfehler:**
   - Versuchen Sie einen anderen Scan-Pfad
   - Stellen Sie sicher, dass Sie Leserechte für das Zielverzeichnis haben

4. **Langsame Scans:**
   - Wählen Sie einen spezifischeren Pfad statt des gesamten Home-Verzeichnisses
   - Schließen Sie große Verzeichnisse wie `node_modules` aus

### Debug-Modus

Für detailliertes Debugging können Sie die Anwendung mit erhöhter Ausgabe starten:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Anpassungen

### Ausgeschlossene Verzeichnisse erweitern

```python
scanner = GitScanner()
scanner.add_excluded_dir('my_large_folder')
scanner.add_excluded_dir('.cache')
```

### Scan-Tiefe begrenzen

```python
repos = scanner.scan("/path", max_depth=5)
```

## Beitragen

1. Fork des Repositories erstellen
2. Feature-Branch erstellen (`git checkout -b feature/amazing-feature`)
3. Änderungen committen (`git commit -m 'Add amazing feature'`)
4. Branch pushen (`git push origin feature/amazing-feature`)
5. Pull Request erstellen

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe `LICENSE` für Details.

## Changelog

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

## Bekannte Einschränkungen

- Sehr große Verzeichnisstrukturen können lange Scan-Zeiten verursachen
- Git-Repositories in symbolisch verlinkten Verzeichnissen werden möglicherweise nicht erkannt
- Windows-Pfade mit Umlauten könnten Probleme verursachen

## Support

Bei Problemen oder Fragen erstellen Sie bitte ein Issue im Repository oder kontaktieren Sie den Entwickler.

---

**Hinweis**: Diese Anwendung führt nur lesende Git-Operationen aus und nimmt keine Änderungen an Ihren Repositories vor.