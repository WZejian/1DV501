i = int(input("Enter an integer: "))
k = 1
sum = 1

if i < 0:
    print("The integer must be a positive.")
else:
    while sum < i:
        k = k + 2
        sum = sum + k
    print(k, "is the smallest k such that 1+3+5+...>=", i)
