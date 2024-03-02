# Write a program  containing a function  returning a count of all
# lines in all Python files in the directory and all its subdirectories


import os


def is_hidden(entry):     # A function check if it is hidden
    a = entry.name.startswith('.')
    b = entry.name.startswith('_')
    return a or b


no_line = 0    # Global variable(number of lines)


# A funtion return number of lines of all python file in the directory
# and its subdirectories
def count_py_lines(dir_path):
    global no_line
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.name.endswith('.py'):    # Specified for python file
            path = entry.path
            with open(path) as file:   # Read python file path
                for line in file:
                    if line != '\n':   # Check if the line is empty
                        no_line += 1
        elif entry.is_dir():
            count_py_lines(entry.path)  # Recursive call
    return no_line


# Current working directory containning all The assignment 2 and 3 files
path = os.getcwd()
number_of_lines = count_py_lines(path)
print(number_of_lines)
