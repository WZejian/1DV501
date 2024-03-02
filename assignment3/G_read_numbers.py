# reads the two files (one after each other) and for each file computes and
# presents the average (mean) value and the standard deviation.

import os
import math


def mean(lst):     # average value
    average = sum(lst)/len(lst)
    return round(average, 1)


def std(lst):      # standard deviation
    lst2 = []
    for n in lst:
        lst2.append((n-mean(lst))**2)
        std = math.sqrt(sum(lst2)/len(lst))  # formula of standard deviation
    return round(std, 1)


path_1 = os.getcwd()
path_1 += '/Test/10000_integers/file_10000integers_A.txt'
with open(path_1) as file:    # open file path_1 for reading
    lst_a = []
    for line in file:
        lst = line.split(',')     # String of each line to a list
        for n in lst:
            lst_a.append(int(n))

path_2 = os.getcwd()
path_2 += '/Test/10000_integers/file_10000integers_B.txt'
with open(path_2) as file:    # open file path_2 for reading
    lst_b = []
    string = file.read()
    lst = string.split(':')     # String of text to a list
    lst_b = [int(n) for n in lst]   # list comprehension


print(f'file_A: mean value({mean(lst_a)}); standard deviation({std(lst_a)})')
print(f'file_B: mean value({mean(lst_b)}); standard deviation({std(lst_b)})')
print()
