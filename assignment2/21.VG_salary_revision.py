# Presenting the average salary, the median salary, and the salary gap

pro_sal = input("Provide salaries：")
words = pro_sal.split()          # use split() to seperate words
sal = [int(w) for w in words]    # Use list comprehension

sal.sort()            # New list containing salaries in ascending order

n = len(sal)           # n elements in the list
if len(sal) % 2 == 0:  # The number of elements in the list is even number
    # median salary is the average of two middle salary in the list
    median = round((sal[round(n/2-1)] + sal[round(n/2)])/2)
else:                 # Odd number of elements in the list
    median = sal[round(n/2)]

print("Median:", median)


sum = sum(sal[::])    # Add all salaries in the list

average = round(sum/n)
print("Average:", average)
gap = sal[len(sal)-1] - sal[0]      # Highest salary - lowest salary
print("Gap:", gap)
