# identify individual words in a text and store these words in a separate file


# It may take a while to run this program

import os


def read_file(file_path):
    lst = []
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            lst.append(line.strip())
    return lst     # A list containg strings for each line


def get_words(row):
    w = ''
    for s in row:     # For each string for each line
        for e in s.lower():  # For each element in a string in lower cases
            # An element is number or letter
            if e.isnumeric() or 97 <= ord(e) <= 122:
                w += e
            else:
                if e == "'" or e == "-" or e == " ":
                    w += e
                else:
                    e = " "
                    w += e
    lst = w.split()         # A list containning full_text

    lst_final = []
    for word in lst:
        if len(word) == 1:
            if word == 'a' or word == 'i':
                lst_final.append(word)  # Exclude letter except 'a' & 'i'
        else:
            if word.isalpha():
                lst_final.append(word)    # Excluding numbers

    return lst_final     # A list containning words of full text


def save_words(file_path, words):
    with open(file_path, 'w', encoding="utf-8") as file:
        text = ''
        for word in words:
            text += word + ' '
        file.write(text)      # Write text to a new file


# Read text file of holy_grail.txt
path = os.getcwd()
path_1 = path + '/Test/large_texts/holy_grail.txt'
row = read_file(path_1)
print(f'\nRead {len(row)} lines from file {path_1}')

# Collect words
words = get_words(row)

# Save words in file
outpath = path + f'/output_{len(words)}_words.txt'
save_words(outpath, words)
print(f'Saved {len(words)} words in file {outpath}')  # 10332 words


# Read text files of eng_news_100K-sentences.txt


# It may take a while to run this program
