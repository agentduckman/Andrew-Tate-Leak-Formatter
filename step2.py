import os
import json
from datetime import datetime

# Function to convert epoch timestamp to human-readable format
def convert_timestamp(epoch_ms):
    return datetime.utcfromtimestamp(epoch_ms / 1000).strftime('%Y-%m-%d %H:%M:%S')

# Iterate through all JSON files in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.json'):
        with open(filename, 'r') as file:
            data = json.load(file)
        
        # Recursively traverse and convert timestamps
        def convert_data(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    if key == 'timestamp' and isinstance(value, int):
                        data[key] = convert_timestamp(value)
                    else:
                        convert_data(value)
            elif isinstance(data, list):
                for item in data:
                    convert_data(item)

        convert_data(data)

        # Save the modified JSON data back to the file
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

print("Timestamps have been converted in all JSON files.")

