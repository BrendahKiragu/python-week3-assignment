def calculate_discount(price, discount_percent):

  if discount_percent >= 20 :
    return price - (price * discount_percent/100)
  else:
    return price  

price = float(input("Enter the original price of an item: "))
discount_percent = float(input("Enter the discount precentage: "))
final_price = calculate_discount(price, discount_percent)   
print(f"Your bill is: {final_price:.2f}") 
