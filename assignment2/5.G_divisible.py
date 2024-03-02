# Prints all the numbers from 100 to 200 that are divisible by 4 or 5

count = 0
for i in range(100, 200):
    # Dividable by 4 or 5,not both
    if i % 4 == 0 and i % 5 != 0 or i % 5 == 0 and i % 4 != 0:
        print(i, end=" ")           # 104 105 108 110 ...
        count += 1
        if count % 10 == 0:         # Ten numbers per line
            print("\n", end="")
print()                             # Add line break
