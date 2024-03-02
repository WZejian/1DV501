import os
import functions.get_words_ZW as zw
import functions.read_file as rf

# Read text files
home = os.getcwd()
news_100k = home + '/large_texts/eng_news_100K-sentences.txt'
holy_grail = home + '/large_texts/holy_grail.txt'

# Change to either file above for different result
lines = rf.read_file_macos(holy_grail)

print(f'Read {len(lines)} lines from {holy_grail}')
print()

# Produce a set of words in a text
lst_string = zw.get_words(lines)

set_string = set(lst_string)
print(len(set_string))

# Make a dictionary with 10 top entries:
txt_dict = {}
for word in lst_string:
    if len(word) > 4:
        if word not in txt_dict:
            txt_dict[word] = 0
        txt_dict[word] += 1

frq_srtd_dict = sorted(txt_dict.items(), key=lambda tpl: tpl[1], reverse=True)

for entry in range(10):
    print(frq_srtd_dict[entry])
