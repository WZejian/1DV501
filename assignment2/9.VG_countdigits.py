# prints the number of zeros, odd digits, and even digits of the integer
# for a given large number

# convert integers to a string
n = str(input("Enter a large positive integer: "))

zeros, odd, even = 0, 0, 0
for i in n:
    num = int(i)    # convert the the element in the string to an integer
    if num == 0:
        zeros += 1
    elif num % 2 == 0:
        even += 1
    elif num % 2 == 1:
        odd += 1

print(f"Zeros: {zeros}")
print(f"Even: {even}")
print(f"Odd: {odd}")
