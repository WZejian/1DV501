# Convert seconds given to the same amount of time given in hours, minutes and seconds
s = int(input("Enter a number of seconds: ")) 

# Using integer division and/or modulus
hours = s // (60*60)             
minutes = (s % (60*60)) // 60   
seconds = (s % (60*60)) % 60    

# Using f-strings
print(f"This corresponds to：{hours} hours, {minutes} minutes, {seconds} seconds")   
