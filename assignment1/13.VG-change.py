# Computes a change a customer received in Swedish bills and coins

# Read input
price = float(input("Price: "))
payment = float(input("Payment: "))

change = round(payment - price)  # Using round
print(f"\nchange:{change}")      # Using f-strings and new line

# Using integer division and/or modulus to
# Extract the minimum number of Swedish bills and coins returned to nearest kr
print(f"""1000kr bills: {change//1000}      
 500kr bills: {(change%1000)//500}
 200kr bills: {((change%1000)%500)//200}
 100kr bills: {(((change%1000)%500)%200)//100}
  50kr bills: {(((change%1000)%500)%200)//100}
  20kr bills: {(((((change%1000)%500)%200)%100)%50)//20}
  10kr coins: {((((((change%1000)%500)%200)%100)%50)%20)//10}
   5kr coins: {(((((((change%1000)%500)%200)%100)%50)%20)%10)//5}
   2kr coins: {((((((((change%1000)%500)%200)%100)%50)%20)%10)%5)//2}
   1kr coins: {((((((((change%1000)%500)%200)%100)%50)%20)%10)%5)%2}""")
   