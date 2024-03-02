# Compute the sum of three digits provided in a three digit number

# Read input
n = int(input("Provide a three digits number: "))

# Using integer divison and/or modulus to extract a, b, c
a = n // 100        
b = (n % 100) // 10
c = (n % 100) % 10   

# Compute the sum
sum_of_digits = a + b + c                 
print(f"sum of digits: {sum_of_digits}")  # Using f-strings
