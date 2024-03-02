# compute an approximation of pi

from random import uniform
from math import pi, pow

count = 0     # count numbers of points inside circle
n1 = 100
# Randomly generate n points
for i in range(0, n1):
    x = uniform(-1, 1)
    y = uniform(-1, 1)

    if pow(x, 2) + pow(y, 2) <= 1:     # Points inside the circle
        count += 1       # count numbers of points inside circle

appr_pi = 4 * count/n1       # Compute appr_pi according to the ratio
error = abs(appr_pi - pi)    # absolute value using abs
print(f"when N = {n1} , approximation of pi:", appr_pi, " error:", error)


count = 0
n2 = 10000
for i in range(0, n2):
    x = uniform(-1, 1)
    y = uniform(-1, 1)

    if pow(x, 2) + pow(y, 2) <= 1:
        count += 1

appr_pi = 4 * count/n2
error = abs(appr_pi - pi)
print(f"when N = {n2} , approximation of pi:", appr_pi, " error:", error)


count = 0
n3 = 1000000
for i in range(0, n3):
    x = uniform(-1, 1)
    y = uniform(-1, 1)

    if pow(x, 2) + pow(y, 2) <= 1:
        count += 1

appr_pi = 4 * count/n3
error = abs(appr_pi - pi)
print(f"when N = {n3} , approximation of pi:", appr_pi, " error:", error)
