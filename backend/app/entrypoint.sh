#!/bin/bash
set -e

# If the argument is a Python file, run CLI mode
if [[ "$1" == *.py ]]; then
    echo "Running CLI analysis on: $1"
    python app/analyze_cli.py "$1"
else
    echo "Starting FastAPI server..."
    uvicorn app.main:app --host 0.0.0.0 --port 8000
fi
