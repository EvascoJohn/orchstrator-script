import os, sys, shutil
import sqlite3

ext = sys.argv[1]
folder = sys.argv[2]

file_array = []

if os.path.isdir(folder):
    print(f"Folder '{folder}' exists, moving file")
else:
    print(f"Folder '{folder}' does not exists.")
    if input(f"create {folder} folder? (yes/type any)\n:") == 'yes':
        print(f"creating '{folder}' folder")
        os.mkdir(folder)
        print(f"Folder '{folder}' exists, moving file")

for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)
    if file_ext == ext:
        file_array.append(file)


total_file = len(file_array)
if input(f"are you sure you want to move {total_file} file(s) in {folder}? (yes/type any)\n:") == 'yes':
        for file in file_array:
            shutil.move(file, folder)
        print("files where moved!")