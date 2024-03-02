# Classify a random number in a given range as odd/even and positive/negative

# Import random module from the library
import random                
a = random.randint(-10, 10)         # a is an random integer in the range[-10,10]
print("The generated number is:", a)

# Using boolean expression and integer modulus to classify the number
if a == 0:     
    print("0 is even and neither positive and negative")
elif a > 0 and a % 2 == 0:   # a is positive and can be divided by 2
    print(a, "is even and positive")
elif a > 0 and a % 2 != 0:   # a is positive and cannot be divided by 2
    print(a, "is odd and positive")
elif a < 0 and a % 2 == 0:   # a is negative and can be divided by 2
    print(a, "is even and negative")
else:                        # a is negative and cannot be divided by 2
    print(a, "is odd and negative")
