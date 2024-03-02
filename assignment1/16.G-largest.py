# Extract the largest number in three provided numbers

# Read input
input("Please enter three integers A,B,C.")

# Read input integers A, B, C
a = int(input("Enter A: "))     
b = int(input("Enter B: "))
c = int(input("Enter c: "))

# Using boolean expressions(comparison operators and logic operators)
# Find the largest number
if a > b and a > c:    
    print("The largest number is:", a)
elif b > a and b > c: 
    print("The largest number is:", b)
else:                 
    print("The largest number is:", c)
