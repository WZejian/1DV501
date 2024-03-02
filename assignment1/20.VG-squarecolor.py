# Identify what color a square on a chess board is when input an identifier.

# Read input
iden = input("Enter a chess square identifier (e.g. e5): ")

# Using string indexing
iden_1 = str(iden[0])   # iden_1 is a string
iden_2 = int(iden[1])   # iden_2 is an interger

# If iden_1 is "b" or "d" or "f" or "h", when iden_2 is even, 
# the square is black, otherwise, white
if iden_1 == "b" or iden_1 == "d" or iden_1 == "f" or iden_1 == "h":
    if iden_2 % 2 == 0 and iden_2 < 8:
        print(iden, "is black")

    elif iden_2 % 2 == 1 and iden_2 < 8:
        print(iden, "is white")

    else:
        print("It does not exsit")

# If iden_1 is "a" or "c" or "e" or "g", when iden_2 is even, 
# the square is white, otherwise, black
if iden_1 == "a" or iden_1 == "c" or iden_1 == "e" or iden_1 == "g":
    if iden_2 % 2 == 0 and iden_2 < 8:
        print(iden, "is white")

    elif iden_2 % 2 == 1 and iden_2 < 8:
        print(iden, "is black")

    else:
        print("It does not exist")

else:
    print("It does not exsit")
