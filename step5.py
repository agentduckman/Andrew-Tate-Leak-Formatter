import os
import glob
import re

def load_user_map(user_file_path):
    """
    Load user map from the provided file.
    Returns a dictionary mapping UIDs to human-readable usernames.
    """
    user_map = {}
    try:
        with open(user_file_path, 'r') as user_file:
            for line in user_file:
                uid, username = line.strip().split(maxsplit=1)
                user_map[uid] = username
    except Exception as e:
        print(f"Error reading user file: {e}")
    return user_map

def build_replacement_regex(user_map):
    """
    Build a compiled regex pattern to match all UIDs and a replacement function.
    """
    pattern = re.compile("|".join(re.escape(uid) for uid in user_map.keys()))
    return pattern

def replace_uids_in_file(input_file, user_map, replacement_regex):
    """
    Replace UIDs in the file with human-readable usernames using a compiled regex.
    Overwrites the original file with the updated content.
    """
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Replace UIDs in the content using regex
        content = replacement_regex.sub(lambda match: user_map[match.group(0)], content)

        with open(input_file, 'w') as outfile:
            outfile.write(content)

        print(f"Processed and updated file: {input_file}")
    except Exception as e:
        print(f"Error processing file {input_file}: {e}")

def main():
    # File paths
    user_file = "users.key"  # User mapping file
    input_files = glob.glob("*_formatted.txt")  # All files ending with _formatted.txt

    if not os.path.exists(user_file):
        print("Error: users.key file not found in the current directory.")
        return

    # Load the user map
    user_map = load_user_map(user_file)
    if not user_map:
        print("User map is empty or failed to load.")
        return

    # Build a single regex for UID replacement
    replacement_regex = build_replacement_regex(user_map)

    # Process each matching file
    if not input_files:
        print("No files ending with '_formatted.txt' found in the current directory.")
        return

    for input_file in input_files:
        replace_uids_in_file(input_file, user_map, replacement_regex)

if __name__ == "__main__":
    main()

