# A function to build a BST data structure from a list
import functions.BstMap as bst


def build_bst(lst):
    Bst = bst.BstMap()
    for word in lst:
        if Bst.get(word) is None:
            Bst.put(word, 1)
        else:
            value = Bst.get(word) + 1
            Bst.put(word, value)
    return Bst
