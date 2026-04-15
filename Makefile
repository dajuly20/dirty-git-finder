.PHONY: help install install-dev install-user uninstall run build clean publish test lint autostart autostart-remove

# Default target
help:
	@echo "Dirty Git Finder - Makefile"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install        Install system-wide (requires sudo)"
	@echo "  install-user   Install for current user only (~/.local/bin)"
	@echo "  install-dev    Install in development mode (editable)"
	@echo "  uninstall      Uninstall the application"
	@echo "  run            Run the application"
	@echo "  build          Build the Python package"
	@echo "  publish        Publish to PyPI (requires twine)"
	@echo "  publish-test   Publish to TestPyPI"
	@echo "  clean          Remove build artifacts"
	@echo "  autostart      Enable autostart on login"
	@echo "  autostart-remove  Disable autostart"
	@echo "  lint           Run code linting"
	@echo "  test           Run tests"
	@echo ""

# Run the application
run:
	.venv/bin/python run.py

# Install system-wide
install:
	pip3 install .

# Install for current user
install-user:
	pip3 install --user .
	@echo ""
	@echo "Installed! Make sure ~/.local/bin is in your PATH"
	@echo "Run with: dirty-git-finder"

# Install in development mode
install-dev:
	pip3 install -e ".[dev]"

# Uninstall
uninstall:
	pip3 uninstall -y dirty-git-finder

# Build the package
build: clean
	.venv/bin/python -m build

# Publish to PyPI
publish: build
	.venv/bin/python -m twine upload dist/*

# Publish to TestPyPI
publish-test: build
	.venv/bin/python -m twine upload --repository testpypi dist/*

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf src/*.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Enable autostart
autostart:
	@./scripts/autostart-install.sh

# Disable autostart
autostart-remove:
	@./scripts/uninstall-autostart.sh

# Lint the code
lint:
	@echo "Running pylint..."
	-pylint src/dirty_git_finder.py src/git_scanner.py
	@echo ""
	@echo "Running flake8..."
	-flake8 src/ --max-line-length=120

# Run tests (placeholder)
test:
	@echo "No tests configured yet"
	@echo "TODO: Add pytest tests"

# Create source distribution only
sdist:
	.venv/bin/python -m build --sdist

# Create wheel only
wheel:
	.venv/bin/python -m build --wheel

# Show version
version:
	@grep -m1 'version' pyproject.toml | cut -d'"' -f2

# Check if ready for publishing
check: build
	python3 -m twine check dist/*
