# Rolling two dice 10000 times, present the frequencies for
# the different numbers of two dice values added.

from random import randint

print("Frequency table (sum,count) for rolling two dices 10000 times")

add_val = []   # added value
for i in range(10000):       # 10000 times two dices rolled
    # Add the sum of two random integers in the list
    add_val.append(randint(1, 6) + randint(1, 6))

# present the frequencies for the different number
for j in range(2, 13):
    print(j, add_val.count(j))
