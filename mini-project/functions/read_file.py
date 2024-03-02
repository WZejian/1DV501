# Function to read lines in a file

def read_file_windows(file_path):
    lst = []
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            lst.append(line.strip())
    return lst


def read_file_macos(path):
    line_lst = []
    with open(path, "r") as file:
        for line in file:
            line_lst.append(line.strip())
    return line_lst
