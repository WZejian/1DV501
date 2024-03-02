# gives an indented print where the directory depth is given by the
# indentation (see example below) and avoids printing hidden directories

import os


def is_hidden(entry):    # Check if hidden or not
    a = entry.name.startswith('.')
    b = entry.name.startswith('_')
    return a or b


count = 0       # Global variable


def print_subdirectories(dir_path):
    global count       # Used for control the indention when recursion
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir() and not is_hidden(entry):  # check if it is a folder
            print(count * '    ', end='')
            print(entry.name)
            count += 1
            print_subdirectories(entry.path)   # Recursive call
            count -= 1


path = os.getcwd()
print_subdirectories(path)
