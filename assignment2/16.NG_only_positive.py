print("Enter positive integers. End by giving a negative integer.")

n = 0
pos = []
while True:
    ints = int(input(f"Integer {n+1}: "))
    if ints > 0:
        n += 1
        pos.append(ints)
    else:
        break

print("Number of positives:", n)
print("Positive numbers: ", pos)
