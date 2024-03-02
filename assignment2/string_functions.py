# Define functions


# A function that returns the result of concatenating
# the string s with itself n times
def concat(s, n):
    for i in range(n):
        print(s, end="")
    print()


# A function that returns the number of times the character x
# occurs in the string s
def count(s, x):
    n = 0
    for c in s:
        if c == x:
            n += 1
    return n


# A function that returns a string with all the characters in s
# in reverse order
def reverse(s):
    for i in range(len(s)-1, -1, -1):
        print(s[i], end="")
    print()


# A function that returns the first and last characters in the string s
def first_last(s):
    fir_ch = s[0]
    las_ch = s[-1]
    return fir_ch, las_ch


# A function that return True if the string contains exactly two instances
# of the character X, otherwise False.
def has_two_X(s):
    n = 0
    for c in s:
        if c == "X":
            n += 1
    if n == 2:
        return True
    else:
        return False


# A function that returns True if the string s
# contains any duplicate characters, otherwise False.
def has_duplicates(s):
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return True
    return False
