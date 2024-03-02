# Extract the first letter in the first name and 
# first four letters in the given name

# Read input
first_name = input("First name: ")
given_name = input("Given name: ")

# Using string dexing
# Extract character at position 0 in the first name and 
# characters from position 0 to 3 in the given name
print(f"{first_name[0]}. {given_name[0:4]}")   
