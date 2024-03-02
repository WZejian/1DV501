# A function to build a Hash Set from a list
import functions.HashSet as hs


def build_hash(lst):
    words = hs.HashSet()   # Create new empty HashSet
    words.init()
    for item in lst:
        words.add(item)
    return words
