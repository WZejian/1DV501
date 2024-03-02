# Prints two triangles

import sys


n = int(input("Enter an positive odd integer: "))
if n < 1 or n % 2 == 0:
    print("Follow the instruction!\n")
    sys.exit()     # Terminates program execution


# right-angled triangle
print("Right-Angled triangle:")
lines_1 = ""
for i in range(n):
    lines_1 = i*" " + (n-i)*"*"
    print(lines_1)


# Isosceles Triangle
print("\nIsosceles triangle:")
lines_2 = ""
for i in range(1, n+1):
    if i % 2 == 1:
        lines_2 = ((n-i)//2)*" " + i*"*" + ((n-i) // 2)*" "
        print(lines_2)
