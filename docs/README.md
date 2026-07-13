# Dirty Git Repository Finder

Scannt dein System nach Git-Repositories und zeigt, welche "dirty" sind (uncommitted changes, kein Remote, unpushed commits).

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)

---

## Schnellstart

### Installation

```bash
# Mit pipx (empfohlen - isolierte Umgebung)
pipx install git+https://github.com/dajuly20/scan-for-dirty-git-repos-gui.git

# Oder mit pip
pip install git+https://github.com/dajuly20/scan-for-dirty-git-repos-gui.git
```

### Nutzung

```bash
dirty-git-finder      # GUI starten
git-dirty             # CLI (scannt aktuelles Verzeichnis)
git-dirty ~/projects  # CLI mit Pfad
git-dirty --gui       # CLI mit GUI-Flag
dirty-git --dirty-only # Nur dirty Repos anzeigen
```

---

## Features

- **GUI & CLI**: Grafische Oberflaeche oder Kommandozeile
- **Rekursiver Scan**: Durchsucht alle Unterverzeichnisse
- **Dirty-Erkennung**: Uncommitted changes, kein Remote, unpushed commits
- **Einstellbare Kriterien**: Checkboxen fuer Dirty-Definition
- **Kontextmenue**: Git Graph, VS Code, Terminal, Push/Pull
- **Cross-Platform**: Linux, macOS, Windows

---

## Installation (Details)

### Voraussetzungen

- Python 3.8+
- tkinter (fuer GUI)
- Git

```bash
# Ubuntu/Debian
sudo apt install python3 python3-tk git

# macOS
brew install python-tk git

# Windows: Python von python.org, Git von git-scm.com
```

### Methode 1: pipx/pip von GitHub

```bash
pipx install git+https://github.com/dajuly20/scan-for-dirty-git-repos-gui.git
```

### Methode 2: Aus Release-Datei

1. [Release herunterladen](https://github.com/dajuly20/scan-for-dirty-git-repos-gui/releases)
2. Wheel installieren:
```bash
pip install dirty_git_finder-*-py3-none-any.whl
```

### Methode 3: Entwicklermodus

```bash
git clone https://github.com/dajuly20/scan-for-dirty-git-repos-gui.git
cd scan-for-dirty-git-repos-gui
pip install -e .
```

---

## CLI-Optionen

```
git-dirty [PATH] [OPTIONS]

Positional:
  path                  Pfad zum Scannen (Standard: aktuelles Verzeichnis)

Optionen:
  --gui, -g             GUI starten
  --dirty-only, -d      Nur dirty Repositories
  --clean-only, -c      Nur clean Repositories
  --uncommitted         Nur mit uncommitted changes
  --no-remote           Nur ohne Remote
  --unpushed            Nur mit unpushed commits
  --json                JSON-Ausgabe
  --quiet               Keine Fortschrittsanzeige
  --max-depth N         Maximale Scan-Tiefe
```

---

## GUI-Bedienung

### Hauptfenster

| Element | Funktion |
|---------|----------|
| Scan Path | Zu durchsuchender Pfad |
| Start/Cancel | Scan starten/abbrechen |
| Filter | All / Dirty Only / Clean Only |
| Dirty-Kriterien | Checkboxen: Uncommitted, No Remote, Unpushed |

### Ergebnistabelle

| Spalte | Inhalt |
|--------|--------|
| Name | Repository-Name |
| Path | Vollstaendiger Pfad |
| Branch | Aktueller Git-Branch |
| Status | DIRTY / CLEAN |
| Changes | Aenderungen + Warnungen |
| Aelteste Aenderung | Datei + Zeitstempel |
| Letzter Commit | Commit-Zeitpunkt |

### Kontextmenue (Rechtsklick)

- Git Graph anzeigen
- Push & Pull ausfuehren
- Remote URL oeffnen
- In VS Code oeffnen
- Terminal oeffnen

---

## Dirty-Kriterien

Ein Repository gilt als "dirty" wenn mindestens eines der aktivierten Kriterien zutrifft:

| Kriterium | Standard | Beschreibung |
|-----------|----------|--------------|
| Uncommitted changes | AN | Modified, added, deleted, untracked files |
| No remote | AN | Kein Remote (GitHub/GitLab) konfiguriert |
| Unpushed commits | AUS | Lokale commits nicht gepusht |

---

## Projektstruktur

```
scan-for-dirty-git-repos-gui/
├── pyproject.toml          # Paket-Konfiguration
├── run.py                  # Launcher
├── src/
│   ├── dirty_git_finder.py # GUI-Anwendung
│   ├── git_dirty_cli.py    # CLI
│   └── git_scanner.py      # Scanner-Modul
├── assets/                 # Icons
├── scripts/                # Shell-Skripte
└── docs/                   # Dokumentation
```

---

## Entwicklung

```bash
# Repository klonen
git clone https://github.com/dajuly20/scan-for-dirty-git-repos-gui.git
cd scan-for-dirty-git-repos-gui

# Entwicklermodus
pip install -e ".[dev]"

# Direkt starten
python run.py

# Paket bauen
python -m build
```

### Makefile-Befehle

```bash
make run            # Anwendung starten
make build          # Paket bauen
make install-user   # Fuer aktuellen Benutzer installieren
make clean          # Build-Artefakte loeschen
```

---

## Changelog

### v2.2.1 (2026-07-13)
- Fix: Paketstruktur fuer pip/pipx Installation korrigiert
- GitHub Actions: Automatisierte Releases

### v2.2.0 (2026-04-15)
- CLI mit `git-dirty` und `dirty-git` Befehlen
- `--gui` Flag fuer CLI
- Makefile fuer Build-Automatisierung

### v2.1.0 (2026-02-12)
- Einstellbare Dirty-Kriterien (Checkboxen)
- Unpushed-Commits-Erkennung

### v2.0.0 (2026-02-12)
- Remote-Check: Repos ohne Remote als dirty markieren
- Projektstruktur reorganisiert

---

## Lizenz

MIT License

---

## Links

- [GitHub Repository](https://github.com/dajuly20/scan-for-dirty-git-repos-gui)
- [Releases](https://github.com/dajuly20/scan-for-dirty-git-repos-gui/releases)
- [Issues](https://github.com/dajuly20/scan-for-dirty-git-repos-gui/issues)
