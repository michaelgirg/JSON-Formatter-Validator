import json

def format_json(json_str):
    parsed = json.loads(json_str)
    return json.dumps(parsed, indent=4)

def main():
    print("🔧 JSON Formatter & Validator")
    filename = input("Enter the JSON file name (e.g., data.json): ")
    try:
        with open(filename, "r") as file:
            content = file.read()
            formatted = format_json(content)
            output_file = filename.replace(".json", "_formatted.json")
            with open(output_file, "w") as out:
                out.write(formatted)
            print(f"Formatted JSON saved to {output_file}")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
