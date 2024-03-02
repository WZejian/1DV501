# Generates and prints n random numbers in the interval [1,100]
# Prints the average value, the smallest number, and the largest number.

import random
import sys

n = int(input("Enter number of integers generated: "))
if n < 1:
    print("Number must be positive.")
    sys.exit()       # Terminates program execution

sum = max = min = average = 0
print("Generated Values: ", end="")
for i in range(1, n + 1):
    rn = random.randint(1, 100)    # random integer generated
    print(rn, end=" ")
    sum = sum + rn
    average = sum/i      # compute average value

    # Determining maximum and minimum value
    if i == 1:
        min = max = rn
    else:
        if rn > max:
            max = rn
        elif rn < min:
            min = rn
print()     # add line break
print(f"Average, min, max are: {round(average,2)}, {min} and {max}")
