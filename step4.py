import re
from datetime import datetime
import os

def process_chatlog(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    consolidated_lines = []
    current_entry = ""

    # Consolidate multi-line messages into single lines
    for line in lines:
        if re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line):
            if current_entry:
                consolidated_lines.append(current_entry)
            current_entry = line.strip()
        else:
            current_entry += " " + line.strip()
    
    if current_entry:
        consolidated_lines.append(current_entry)

    # Sort the consolidated lines by timestamp
    sorted_lines = sorted(consolidated_lines, key=lambda x: datetime.strptime(x[:19], '%Y-%m-%d %H:%M:%S'))

    # Overwrite the original file with the sorted lines
    with open(input_file, "w") as file:
        for line in sorted_lines:
            file.write(line + "\n")

# Process all files in the current directory that end with _formatted.txt
for file_name in os.listdir("."):
    if file_name.endswith("_formatted.txt"):
        print(f"Processing {file_name} and overwriting it with sorted data.")
        process_chatlog(file_name)

