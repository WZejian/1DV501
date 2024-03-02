def is_odd(n):
    if n % 2 == 0:
        print(n, "is not an odd number.")
    else:
        print(n, "is an odd number")


def sum(m, n):
    s = 0
    for i in range(m, n+1):
        s = s + i
    return s


def contains(s, c):
    for i in s:
        if i == c:
            return True
        else:
            return False


def test_and_print(s, c):
    if contains(s, c):
        print(s, "contains 'c'")
    else:
        print(s, "does not contain 'c'")


test_and_print("calculation", "c")
test_and_print("jjjj", "c")


def multi_print(s, n):
    for i in range(0, n):
        print(s, end=">")


multi_print("Good", 3)
