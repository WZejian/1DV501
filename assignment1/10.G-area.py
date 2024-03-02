# Computes area of a circle given a radius
radius = float(input("Enter a radius of a circle: "))   
pi = 3.141593

a = pi*radius**2      # Compute area                                 
print(f"Circle area: {round(a,1)}")  # Using f-strings
