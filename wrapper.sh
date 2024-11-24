#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Starting the execution of scripts..."

# Step 1: Execute step1.sh
echo "Executing step1.sh..."
./step1.sh
echo "Completed step1.sh."

# Step 2: Execute step2.py
echo "Executing step2.py..."
python3 step2.py
echo "Completed step2.py."

# Step 3: Execute step3.py
echo "Executing step3.py..."
python3 step3.py
echo "Completed step3.py."

# Step 4: Execute step4.py
echo "Executing step4.py..."
python3 step4.py
echo "Completed step4.py."

# Step 4.5: Cleanup old .json files
rm ./*.json
echo "Original .json files deleted"

# Step 5: Replace usernames
echo "Executing step5.py"
echo "Replacing UIDs with usersnames"
python3 step5.py
echo "Completed step 5"

echo "All scripts executed successfully!"

