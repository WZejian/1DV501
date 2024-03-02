# computes the largest integer k such that 0+2+4+6+8+...+k < n

n = int(input("Enter a positive integer: "))

if n < 0:
    print("Integer must be positive.")

else:
    s = 0                 # sum
    k = 0
    while s < n:
        k = k + 2         # k = 0, 2, 4, ...
        s = s + k         # s = 0, 2, 6, ...
    k = k - 2

    print(k, "is the largest k such that 0+2+4+...+k <", n)
