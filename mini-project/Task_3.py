import os
import functions.get_words_ZW as gw
import functions.read_file as rf
import functions.top_10 as top10
import functions.build_BST as bld_bst
import functions.build_hash as bld_hash

# Read text files
home = os.getcwd()
news_100k = home + '/large_texts/eng_news_100K-sentences.txt'
holy_grail = home + '/large_texts/holy_grail.txt'

# Please use read_file_windows for windows
# And use read_file_macos for macos

# Make list of word for 100K
file_100k = rf.read_file_macos(news_100k)
lst_100k = gw.get_words(file_100k)

# Make list of words Holy Grail
file_HG = rf.read_file_macos(holy_grail)
lst_HG = gw.get_words(file_HG)


# Main Body


# Create HashSet and BST:
hash100k = bld_hash.build_hash(lst_100k)
bst100k = bld_bst.build_bst(lst_100k)

hashHG = bld_hash.build_hash(lst_HG)
bstHG = bld_bst.build_bst(lst_HG)

# Count unique words and print top 10 (100K)
print('File: eng_news_100K-sentences.txt')
print(hash100k.get_size())
top10.top_10(bst100k)

# Max bucket size for HS and max depth for BST (100k)
print(f"Max bucket size in Hash Table is: {hash100k.max_bucket_size()}")
print(f"Max depth of BST is: {bst100k.max_depth()}")
print()

# Count unique words and print top 10 (Holy Grail)
print('File: holy_grail.txt')
print(hashHG.get_size())
top10.top_10(bstHG)

# Max bucket size for HS and max depth for BST (Holy Grail)
print(f"Max bucket size the Hash Table is: {hashHG.max_bucket_size()}")
print(f"Max depth of BST is: {bstHG.max_depth()}")
print()
