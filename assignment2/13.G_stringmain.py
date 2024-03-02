# Make funtions defined in string_functions availble

from string_functions import reverse, concat, count
from string_functions import first_last, has_duplicates, has_two_X


s = "XXxoutside"


rev = reverse(s)         # reverse a string


concat(s, 3)             # concatenate  a string 3 times


print("Number of 'x':", {count(s, 'x')})     # count "x"


fir_ch, las_ch = first_last(s)
print("First character is:", fir_ch, ", Last character is:", las_ch)


if has_duplicates(s):     # if has_duplicates(s) is True
    print(s, "has duplicates.")
else:                     # False
    print(s, "has no duplicates")


if has_two_X(s):          # if has_two_X(s) is True
    print(s, "has two X")
else:                     # False
    print(s, "does not have two X")
