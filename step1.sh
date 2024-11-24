#!/bin/bash

# Check if jq is installed
if ! command -v jq &> /dev/null; then
  echo "jq is not installed. Please install jq to use this script."
  exit 1
fi

# Process each .json file in the current directory
for file in *.json; do
  # Ensure we are working with a file
  [ -f "$file" ] || continue

  echo "Processing: $file"

  # 1. Pretty format the JSON
  jq . "$file" > temp.json && mv temp.json "$file"

  # 2. Remove lines that are only "["
  sed -i '/^\[\s*$/d' "$file"

  # 3. Remove lines that are only "]"
  sed -i '/^\]\s*$/d' "$file"

  # 4. Replace lines that are only "  }" with "  },"
  sed -i 's/^  }\s*$/  },/' "$file"

  # 5. Insert "[" as the first line
  sed -i '1i [' "$file"

  # 6. Insert "]" as the last line
  sed -i -e '$a ]' "$file"

  # 7. Remove trailing comma on second-to-last line
  sed -i "$(($(wc -l < "$file") - 1))s/,//g" "$file"
done

echo "All .json files have been processed."

