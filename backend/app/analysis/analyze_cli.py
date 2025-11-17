#!/usr/bin/env python3
import sys
import json
from .model import analyze_file   # update import if needed

def main():
    if len(sys.argv) < 2:
        print("Usage: analyze_cli.py <file1> <file2> ...")
        sys.exit(1)

    files = sys.argv[1:]

    results = {}
    for f in files:
        try:
            output = analyze_file(f)
            results[f] = output
        except Exception as e:
            results[f] = {"error": str(e)}

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
