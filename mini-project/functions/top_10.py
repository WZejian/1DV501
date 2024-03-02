# A supporting function to find top 10 items from a BST


def top_10(bst_tree):
    top_10_sort = []
    top_10_sort = sorted(bst_tree.as_list(), key=lambda x: x[1], reverse=True)

    counter = 0
    for entry in top_10_sort:
        if len(entry[0]) > 4:
            print("(" + entry[0], end=', ')
            print(str(entry[1]) + ")")
            counter += 1
        if counter == 10:
            break
