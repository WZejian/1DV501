# computes the value of savings after 5 years given a certain interest rate 
s = int(input("Enter your initial savings: "))           
p = int(input("Enter interest rate in percentage: "))  

# Using ** (raised to)
savings_after_5_years = s*(1 + p/100)**5   # computes savings after 5 years

# Using f-strings 
print(f"The value of your savings after 5 years is: {round(savings_after_5_years ) }")             
