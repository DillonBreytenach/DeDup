import os

# Set the current directory path
current_dir_path = os.getcwd()

# Get the list of files and directories in the current directory
entries = os.listdir(current_dir_path)

# Iterate over the list of entries and delete everything except for the "de_dupped" directory
for entry in entries:
    if entry != "de_dupped":
        entry_path = os.path.join(current_dir_path, entry)
        if os.path.isfile(entry_path):
            os.remove(entry_path)
        else:
            shutil.rmtree(entry_path)

