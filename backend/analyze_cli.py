import sys
import json
from main import analyze_file  

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No file path provided"}))
        return

    file_path = sys.argv[1]
    result = analyze_file(file_path)
    print(json.dumps(result))

if __name__ == "__main__":
    main()
