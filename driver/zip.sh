#!/bin/bash

# Get the script's directory path (using robust method)
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Read a folder path from the user (optional)
read -p "Enter the folder path (or press Enter to use script location): " folder_path

# If folder path is empty, use script directory
if [[ -z "$folder_path" ]] ; then
  folder_path="$script_dir"
fi

# Check if folder exists
if [[ ! -d "$folder_path" ]]; then
  echo "Error: Folder '$folder_path' does not exist."
  exit 1
fi

# Zip all files in the folder
zip -r "$folder_path/2345.zip" "$folder_path/*"

echo "Successfully zipped files in '$folder_path' to 2345.zip"
