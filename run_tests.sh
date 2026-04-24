#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# run_tests.sh
# CI script: activates the virtual environment and executes the test suite.
# Exits with code 0 if all tests pass, or 1 if any test fails.
# ─────────────────────────────────────────────────────────────────────────────

set -e  # Exit immediately if any command fails

# ── Resolve the directory this script lives in ───────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "============================================"
echo "  Pink Morsel Sales Visualiser — Test Suite"
echo "============================================"

# ── Activate virtual environment ─────────────────────────────────────────────
# Support both Unix (venv/bin/activate) and Windows Git Bash (venv/Scripts/activate)
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
else
    echo "ERROR: Virtual environment not found."
    echo "Please create it first: python -m venv venv && pip install -r requirements.txt"
    exit 1
fi

echo "Virtual environment activated."
echo "Python: $(python --version)"
echo ""

# ── Run the test suite ───────────────────────────────────────────────────────
echo "Running tests..."
echo ""

if python -m pytest test_app.py -v --tb=short; then
    echo ""
    echo "============================================"
    echo "  All tests passed. ✓"
    echo "============================================"
    exit 0
else
    echo ""
    echo "============================================"
    echo "  One or more tests failed. ✗"
    echo "============================================"
    exit 1
fi
