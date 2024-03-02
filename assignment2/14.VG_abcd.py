# Present four different digits A, B, C, and D such that the number DCBA
# is equal to 4 times the number ABCD

# converts digits a, b, c, d into a four digit integer abcd.
def get_number(a, b, c, d):
    return a*1000 + b*100 + c*10 + d


# A quadruple nested loop for number 0 to 9999
for a in range(1, 10):          # a cannot be 0
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(1, 10):      # d cannot be 0
                if get_number(a, b, c, d) == 4 * get_number(d, c, b, a):
                    print("Result is:", a, b, c, d)
