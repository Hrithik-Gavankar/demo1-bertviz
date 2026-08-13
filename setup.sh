#!/usr/bin/env bash
# Automated setup for BertViz demo (macOS / Linux)
set -euo pipefail

cd "$(dirname "$0")"

echo "Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Registering Jupyter kernel (for Jupyter Lab / Notebook)..."
python -m ipykernel install --user --name=demo1-bertviz --display-name="Python (demo1-bertviz)"

echo ""
echo "Verifying setup..."
python verify_setup.py

echo ""
echo "Done."
echo ""
echo "Next steps:"
echo "  Cursor / VS Code : open bertviz_demo.ipynb → kernel → .venv"
echo "  Jupyter Lab      : jupyter lab → kernel → Python (demo1-bertviz)"
echo "  See SETUP.md for full instructions."
