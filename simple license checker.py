# simple_license_checker.py

import os

# Function to check for licenses in files
def check_license(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()

            # Search for license keywords in the content
            if 'mit' in content:
                return "MIT License Found"
            elif 'apache' in content:
                return "Apache License Found"
            elif 'gpl' in content:
                return "GPL License Found"
            else:
                return "License Not Found"
    except Exception as e:
        return f"Error reading file: {e}"

# Function to scan all files in a directory
def scan_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py') or file.endswith('.js'):  # You can add other file types
                file_path = os.path.join(root, file)
                print(f"Checking file: {file_path}")
                license_status = check_license(file_path)
                print(f"License Status: {license_status}\n")

# Usage
if __name__ == "__main__":
    directory_to_scan = input("Enter the directory path to scan: ")
    scan_directory(directory_to_scan)
