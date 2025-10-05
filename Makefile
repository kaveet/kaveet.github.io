# Makefile for local development

.PHONY: help install dev build clean

help:
	@echo "Available commands:"
	@echo "  make install   - Create venv and install dependencies"
	@echo "  make dev       - Start live preview server with auto-reload"
	@echo "  make build     - Build the documentation"
	@echo "  make clean     - Clean build artifacts"

install:
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt
	@echo ""
	@echo "Virtual environment created and dependencies installed."
	@echo "Activate it with: source venv/bin/activate"

dev:
	@if [ ! -d "venv" ]; then \
		echo "Virtual environment not found. Run 'make install' first."; \
		exit 1; \
	fi
	@echo "Starting live preview server at http://127.0.0.1:8000"
	@echo "Press Ctrl+C to stop."
	./venv/bin/sphinx-autobuild docs docs/_build/html --open-browser

build:
	@if [ ! -d "venv" ]; then \
		echo "Virtual environment not found. Run 'make install' first."; \
		exit 1; \
	fi
	cd docs && ../venv/bin/sphinx-build -M html . _build

clean:
	cd docs && rm -rf _build
