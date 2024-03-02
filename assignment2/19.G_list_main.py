# Make funtions defined in list_functions.py availble

from list_functions import random_list, average, only_odd
from list_functions import to_string, contains, has_duplicates

# Make a list containing 6 random integers.
lst1 = random_list(6)
print("The list_1 containning random integers:", lst1)
print()


# Present the average value of numbers in the given list
lst2 = [2, 45, 3, -8, 12]
ave = average(lst2)
print("The average number in list_2 is:", ave)
print()


# Present the odd numbers in the given list
lst3 = [1, 13, 2, 42, 47, 32]
odd = only_odd(lst3)
print("The list_3 contains odd numbers:", odd)
print()


# convert the list to a string
lst4 = [1, 2, 3, 4]
s = to_string(lst4)
print("The list_4 convert to a string: ", s)
print()


# Check if one element  in the list is followed by another element
lst5 = [2, 4, 1, 6, 11]
print("In list_5, 4 followed by 1:", contains(lst5, 4, 1))
print("In list_5, 4 followed by 11:", contains(lst5, 4, 11))
print()


# Check if the list has duplicates
lst6 = [4, 5, 6, 5]
print("The list_6 has duplicates:", has_duplicates(lst6))
print()
