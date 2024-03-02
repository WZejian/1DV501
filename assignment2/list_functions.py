from random import randint


# A function that returns a list containing n random integers
# in the interval 1 to 100.
def random_list(n):
    rd = []
    for i in range(n):
        rd.append(randint(1, 100))
    return rd


# A function returning the average of all values in the list lst.
def average(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    aver = sum/len(lst)
    return(round(aver))


# A function that returns a new list containing only the odd integers in lst
def only_odd(lst):
    odd = [n for n in lst if n % 2 == 1]
    return odd


# A function that returns a comma separated string
# representation of the elements in lst.
def to_string(lst):
    s = str(lst)
    return s


# A function that returns True if 'a' is directly followed by 'b'
# anywhere in the list lst
def contains(lst, a, b):
    while a in lst:
        if lst.index(a) != lst.index(b)-1:  # use index to point the positon
            n = lst.index(a)
            lst = lst[n+1::]          # slicing sequences
        else:
            return True
    return False


# A function that returns True if the list lst contains
# any duplicate elemments, otherwise False.
def has_duplicates(lst):
    for ch in lst:
        if lst.count(ch) != 1:
            return True
    return False
