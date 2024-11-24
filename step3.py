import os
import json

def process_json_file(input_file, output_file):
    # Read the JSON data from the input file
    with open(input_file, "r") as infile:
        messages = json.load(infile)

    # Write the formatted data to the output file
    with open(output_file, "w") as outfile:
        for message in messages:
            timestamp = message.get("timestamp", "N/A")
            author = message.get("author", "N/A")
            content = message.get("content", "N/A")
            outfile.write(f"{timestamp} - {author}: {content}\n\n")

    print(f"Formatted data written to {output_file}")

def process_all_json_files():
    # Get a list of all files in the current directory
    files = os.listdir('.')
    json_files = [file for file in files if file.endswith('.json')]

    # Process each JSON file
    for json_file in json_files:
        print(f"Processing file: {json_file}")
        output_file = f"{os.path.splitext(json_file)[0]}_formatted.txt"  # Create output filename based on input file
        process_json_file(json_file, output_file)

if __name__ == "__main__":
    process_all_json_files()
