# Compute the amount of tax paid when monthly income is given in Sweden

# Read input
inc = int(input("Enter monthly income(kr): "))

# Using boolean expression
if inc < 38000:               # Condition 1
    tax = inc * 0.3           # Compute tax in contion 1
    print("Tax is:", tax)

elif 38000 < inc < 50000:                   # Condition 2
    tax = inc * 0.3 + (inc - 38000) * 0.05  # Compute tax in condition 2
    print("Tax is:", tax)

else:    # Conditon 3 
    # Compute tax in condition 3
    tax = inc * 0.3 + (inc - 38000) * 0.05 + (inc - 50000) * 0.05
    print("Tax is:", round(tax))   
