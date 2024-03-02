counter = 0
for n in range(100, 101):
    if n % 4 == 0 and n % 5 != 0 or n % 4 != 0 and n % 5 == 0:
        counter += 1
        print(n)
        

    
