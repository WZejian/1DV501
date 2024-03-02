# Present seven numbers in the range[1,35] in ascending order
# without duplicates

from random import randint

print("The Lotto numbers this week: ")

lotto = []
n = 0
while n < 7:
    int = randint(1, 35)       # random integer generated
    if int not in lotto:
        lotto.append(int)
        n += 1        # End this iteration, jump to while n < 7

lotto.sort()     # Sort the list in ascending order
print(lotto)
