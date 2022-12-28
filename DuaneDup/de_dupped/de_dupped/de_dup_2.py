import os
import shutil

current_dir_path = os.getcwd()
if not os.path.exists("de_dupped"):
    os.mkdir("de_dupped")

entries = os.listdir(current_dir_path)
size_to_filenames = {}
for entry in entries:
    entry_path = os.path.join(current_dir_path, entry)
    if os.path.isfile(entry_path):
        size = os.path.getsize(entry_path)
        if size not in size_to_filenames:
            size_to_filenames[size] = [entry]
        else:
            size_to_filenames[size].append(entry)

for size, filenames in size_to_filenames.items():
    if len(filenames) > 1:
        latest_filename = max(filenames, key=lambda x: os.stat(os.path.join(current_dir_path, x)).st_mtime)
        for filename in filenames:
            if filename != latest_filename:
                file_path = os.path.join(current_dir_path, filename)
                os.remove(file_path)

non_duplicate_entries = []
for size, filenames in size_to_filenames.items():
    if len(filenames) == 1:
        non_duplicate_entries.extend(filenames)
    else:
        non_duplicate_entries.append(latest_filename)

for entry in entries:
    entry_path = os.path.join(current_dir_path, entry)
    if os.path.isdir(entry_path):
        non_duplicate_entries.append(entry)

non_duplicate_entries.sort(key=lambda x: os.stat(os.path.join(current_dir_path, x)).st_mtime, reverse=True)

for entry in non_duplicate_entries:
    entry_path = os.path.join(current_dir_path, entry)
    if os.path.isfile(entry_path):
        shutil.copy2(entry_path, "de_dupped")
    else:
        shutil.copytree(entry_path, os.path.join("de_dupped", entry))

