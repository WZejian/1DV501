# computes the distance between two points x1,y1 and x2,y2

from math import sqrt, pow      # Make sqrt and pow from math module available


# Function distance defined
def distance(x1, y1, x2, y2):
    d = sqrt(pow((x1-x2), 2) + pow((y1-y2), 2))
    return round(d, 3)


# input the coordinates
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# convert integers to float numbers
x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)

dis = distance(x1, y1, x2, y2)     # Using function distance defined
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {dis}")
