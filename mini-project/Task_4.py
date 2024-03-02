# Plese take note of program's long run time due to huge sample

# Import data types:
import functions.HashSet as hs
import functions.BstMap as bst
# Import custom functions:
import functions.read_file as rf
import functions.get_words_ZW as gw
# Import rest
import matplotlib.pyplot as plt
import os


# Read text files
# Please use windows or macos specific function to read
home = os.getcwd()
news_100k = home + '/large_texts/eng_news_100K-sentences.txt'
file_100k = rf.read_file_macos(news_100k)

# Make list of word for 100K
lst_100k = gw.get_words(file_100k)


# Modified version of func build_bst
def build_bst_modified(lst):
    Bst = bst.BstMap()
    for word in lst:
        temp = len(word)
        if Bst.get(temp) is None:
            Bst.put(temp, 1)
        else:
            value = Bst.get(temp) + 1
            Bst.put(temp, value)
    return Bst


# Main
# Build BST
bst_100k = build_bst_modified(lst_100k)

# hash_100k = bld_hs.build_hash(lst_100k)

# Create a list of entries from a BST
coordinates = sorted(bst_100k.as_list(), key=lambda x: x[0])

# Word Length vs Word Count (BST)
x = [coordinates[n][0] for n in range(len(coordinates))]
y = [coordinates[m][1] for m in range(len(coordinates))]

# Removing outliers
# English words are typically shorter than 30 letters:


# Build Hash set:
hash_100k = hs.HashSet()
hash_100k.init()
num_added = 0
unq_vs_add = []

for word in lst_100k:
    hash_100k.add(word)
    num_added += 1
    temp_tpl = (num_added, hash_100k.get_size())
    unq_vs_add.append(temp_tpl)

w = [unq_vs_add[k][1] for k in range(len(unq_vs_add))]
z = [unq_vs_add[l][0] for l in range(len(unq_vs_add))]

# Initiate Graph
fig, (ax1, ax2) = plt.subplots(1, 2)

# Graph for BST
ax1.bar(x, y)
ax1.set_xticks([i for i in range(0, 16, 2)])
ax1.set_xlim([0, 16])
ax1.set_title('Words over 30 letters not shown')
ax1.set_xlabel('Word Length (letters in a word)')
ax1.set_ylabel('Word Count (words of this length in a text)')
for i in range(12):
    ax1.annotate(str(y[i]), xy=(x[i], y[i]), ha='center', va='bottom')

# Graph for Hash Set
ax2.plot(z, w)
ax2.set_yticks([i for i in range(0, 120001, 20000)])
ax2.set_xticks([i for i in range(0, 2000001, 200000)])
ax2.set_xlabel('Number of Added Words (in millions)')
ax2.set_ylabel('Number of Unique Words')
ax2.set_title('Words added vs unique words at run time')

plt.show()
