# Prints the name of all subdirectories for a given directory and
# moves on (by calling itself) to print all their subdirectories.

import os


def print_subdirectories(dir_path):
    entries = os.scandir(dir_path)     # List of entries
    for entry in entries:
        if entry.is_dir():     # True that entry is a directory
            print(entry.name)
            print_subdirectories(entry.path)   # Recursive function


path = os.getcwd()    # Get current working dirctory

print_subdirectories(path)
