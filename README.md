<img width="60%" alt="Dirty Git Finder Screenshot" src="https://github.com/user-attachments/assets/f03b10ca-8587-4edd-a660-8c6a340457f0" />

# Dirty Git Repository Finder

Scannt dein System nach Git-Repositories und zeigt, welche "dirty" sind (uncommitted changes, kein Remote, unpushed commits).

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)

---

## Installation

```bash
# Mit pipx (empfohlen)
pipx install git+https://github.com/dajuly20/scan-for-dirty-git-repos-gui.git

# Oder mit pip
pip install git+https://github.com/dajuly20/scan-for-dirty-git-repos-gui.git

# Oder Wheel aus Release herunterladen
pip install dirty_git_finder-*-py3-none-any.whl
```

**Voraussetzungen:** Python 3.8+, tkinter, Git

```bash
# Ubuntu/Debian
sudo apt install python3 python3-tk git
```

---

## Nutzung

```bash
dirty-git-finder      # GUI starten
git-dirty             # CLI (scannt aktuelles Verzeichnis)
git-dirty ~/projects  # CLI mit Pfad
git-dirty --gui       # CLI mit GUI-Flag
dirty-git --dirty-only # Nur dirty Repos anzeigen
```

### CLI-Optionen

```
git-dirty [PATH] [OPTIONS]

  --gui, -g             GUI starten
  --dirty-only, -d      Nur dirty Repositories
  --clean-only, -c      Nur clean Repositories
  --uncommitted         Nur mit uncommitted changes
  --no-remote           Nur ohne Remote
  --unpushed            Nur mit unpushed commits
  --json                JSON-Ausgabe
  --max-depth N         Maximale Scan-Tiefe
```

---

## Features

| Feature | Beschreibung |
|---------|--------------|
| **GUI & CLI** | Grafische Oberflaeche oder Kommandozeile |
| **Rekursiver Scan** | Durchsucht alle Unterverzeichnisse |
| **Dirty-Erkennung** | Uncommitted changes, kein Remote, unpushed commits |
| **Einstellbare Kriterien** | Checkboxen zur Definition was "dirty" bedeutet |
| **Kontextmenue** | Git Graph, VS Code, Terminal, Push/Pull |
| **Cross-Platform** | Linux, macOS, Windows |

### Dirty-Kriterien

| Kriterium | Standard | Beschreibung |
|-----------|----------|--------------|
| Uncommitted changes | AN | Modified, added, deleted, untracked files |
| No remote | AN | Kein Remote (GitHub/GitLab) konfiguriert |
| Unpushed commits | AUS | Lokale commits nicht gepusht |

---

## GUI-Bedienung

### Hauptfenster
- **Scan Path**: Zu durchsuchender Pfad
- **Filter**: All / Dirty Only / Clean Only
- **Dirty-Kriterien**: Checkboxen fuer Uncommitted, No Remote, Unpushed

### Kontextmenue (Rechtsklick)
- Git Graph anzeigen
- Push & Pull ausfuehren
- Remote URL oeffnen
- In VS Code oeffnen
- Terminal oeffnen

---

## Entwicklung

```bash
git clone https://github.com/dajuly20/scan-for-dirty-git-repos-gui.git
cd scan-for-dirty-git-repos-gui

# Entwicklermodus
pip install -e ".[dev]"

# Direkt starten
python run.py

# Paket bauen
python -m build
```

---

## Changelog

### v2.2.1 (2026-07-13)
- Fix: Paketstruktur fuer pip/pipx Installation
- GitHub Actions: Automatisierte Releases

### v2.2.0 (2026-04-15)
- CLI mit `git-dirty` und `dirty-git` Befehlen
- `--gui` Flag

### v2.1.0 (2026-02-12)
- Einstellbare Dirty-Kriterien
- Unpushed-Commits-Erkennung

---

## Links

- [Releases](https://github.com/dajuly20/scan-for-dirty-git-repos-gui/releases)
- [Issues](https://github.com/dajuly20/scan-for-dirty-git-repos-gui/issues)
- [Ausfuehrliche Dokumentation](docs/README.md)

---

**Lizenz:** MIT
