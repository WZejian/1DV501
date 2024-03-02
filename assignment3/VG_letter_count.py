# count the number of times each letter (a-z, upper case letters are
# counted as lower case letters) is occurring in the files

import os

path = os.getcwd()
path_1 = path + '/output_10332_words.txt'    # Holy_grail.txt
path_2 = path + '/output_1916471_words.txt'  # Eng_news_100k-sentences.txt

# letter count for Holy_grail.txt
print('Reading text from the file:holy_grail.txt')
lst = []
with open(path_1, encoding='utf-8') as file:  # open file for reading
    for line in file:
        lst.append(line.strip())  # A list containning each line in the file

lst_final = []
for s in lst:        # for each string in the list
    for e in s:      # for each element in the list
        if e.isalpha():
            if e != " ":
                lst_final.append(e)   # A list containning each letter in file

no_letters = len(lst_final)     # Number of letters in the list
print(f'Total number of letters: {no_letters}')


count = {}     # Empty dictionary
for c in lst_final:
    if c not in count:
        count[c] = 0
    count[c] += 1     # update count for key c for count dictionary

# Sorting dictionaries using lambda
key_sorted = sorted(count.items(), key=lambda tpl: tpl[0])
print('Histogram (where each star represents 50 occurrences of '
      'the given letters\n')
for i in range(26):    # 26 different English letters
    print(key_sorted[i][0], '|', '*' * ((key_sorted[i][1])//50))
print()

# Letter count for eng_news_100-sentences.txt
print('Reading text from the file:eng_news_100-sentences.txt')
lst = []
with open(path_2, encoding='utf-8') as file:
    for line in file:
        lst.append(line.strip())  # A list containning each line in the file

lst_final = []
for s in lst:
    for e in s:
        if e.isalpha():
            if e != " ":
                lst_final.append(e)  # A list containning each letter in file

no_letters = len(lst_final)    # Number of letters in the list
print(f'Total number of letters: {no_letters}')

count = {}
for c in lst_final:
    if c not in count:
        count[c] = 0
    count[c] += 1   # update count for key c for the count dictionary

# Using lambda to sort the dictionary
key_sorted = sorted(count.items(), key=lambda tpl: tpl[0])
print('Histogram (where each star represents 10000 occurrences of the given '
      'letters)\n')
for i in range(26):    # 26 different English letters
    print(key_sorted[i][0], '|', '*' * ((key_sorted[i][1])//10000))
