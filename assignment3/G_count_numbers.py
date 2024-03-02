# Computes and presents the number of different integers and
# the 5 most frequently occurring number
import os


# count and return the number of different integers in the list
def count_different(lst):
    st = set()      # An empty set
    for n in lst:
        if n not in st:
            st.add(n)
    return len(st)


# returns a dictionary (number and count) containing the number of times
# each integer occurs the list
def count_occurrences(lst):
    count = {}
    for n in lst:
        if n not in count:
            count[n] = 0
        count[n] += 1
    return count


# file_10000integers_A.txt
path_1 = os.getcwd()
path_1 += '/Test/10000_integers/file_10000integers_A.txt'
with open(path_1) as file:
    lst_a = []
    for line in file:
        lst = line.split(',')
        for n in lst:
            lst_a.append(int(n))  # A list containning all numbers in the file

n = count_different(lst_a)
print(f'File_10000integers_A: number of different integers: {n}')
dct1 = count_occurrences(lst_a)

# Sorting Dictionaries using Lambdas
value_sorted_1 = sorted(dct1.items(), key=lambda tpl: tpl[1])

# 5 most frequently occurring number
print('5 most frequently occurring numbers are:')
for i in range(len(value_sorted_1)-1, len(value_sorted_1)-6, -1):
    print(value_sorted_1[i][0],  f' {value_sorted_1[i][1]} times')
print()


# file_10000integers_B.txt
path_2 = os.getcwd()
path_2 += '/Test/10000_integers/file_10000integers_B.txt'
with open(path_2) as file:
    lst_b = []
    string = file.read()
    lst = string.split(':')
    lst_b = [int(n) for n in lst]  # A list containning all numbers in the file

n = count_different(lst_b)
print(f'File_10000integers_B:number of different integers: {n}')
dct2 = count_occurrences(lst_b)

# Sorting Dictionaries using Lambdas
value_sorted_2 = sorted(dct2.items(), key=lambda tpl: tpl[1])

# 5 most frequently occurring number
print('5 most frequently occurring numbers are:')
for i in range(len(value_sorted_2)-1, len(value_sorted_2)-6, -1):
    print(value_sorted_2[i][0], f' {value_sorted_2[i][1]} times')
