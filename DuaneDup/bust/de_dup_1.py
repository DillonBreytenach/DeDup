import os
import shutil

# Set the current directory path
current_dir_path = os.getcwd()

# Check if the "de_dupped" directory already exists
if not os.path.exists("de_dupped"):
    # Create a new directory called "de_dupped" if it does not exist
    os.mkdir("de_dupped")

# Get the list of files in the current directory
files = os.listdir(current_dir_path)

# Create a dictionary to store the file sizes and their corresponding filenames
size_to_filenames = {}

# Iterate over the list of files and add the size and filename to the dictionary
for file in files:
    file_path = os.path.join(current_dir_path, file)
    size = os.path.getsize(file_path)
    if size not in size_to_filenames:
        size_to_filenames[size] = [file]
    else:
        size_to_filenames[size].append(file)

# Iterate over the dictionary and delete the duplicate filenames
for size, filenames in size_to_filenames.items():
    if len(filenames) > 1:
        # Find the filename with the latest modification time
        latest_filename = max(filenames, key=lambda x: os.stat(os.path.join(current_dir_path, x)).st_mtime)
        # Delete all the other filenames
        for filename in filenames:
            if filename != latest_filename:
                file_path = os.path.join(current_dir_path, filename)
                os.remove(file_path)

# Sort the list of files by modification time
files.sort(key=lambda x: os.stat(os.path.join(current_dir_path, x)).st_mtime, reverse=True)

# Copy the non-duplicate files to the "de_dupped" directory
for file in files:
    file_path = os.path.join(current_dir_path, file)
    shutil.copy2(file_path, "de_dupped")

