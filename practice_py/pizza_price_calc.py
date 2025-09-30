pizza_prices = {"small": 15, "medium": 20, "large": 25}
pepper_prices = {"small": 2, "medium": 3, "large": 3}
extra_cheese_price = 1

size = input("Enter the size of the pizza - small / medium / large:  ").lower()
add_pepper = input("Do you want to add pepper (y/n)? ").lower()
add_extra_cheese = input("Do you want to add extra cheese (y/n)? ").lower()
#base price
bill = pizza_prices[size]

#add price for extra pepper
if add_pepper == "y":
    bill += pepper_prices[size]

#add price for extra cheese
if add_extra_cheese == "y":
    bill += extra_cheese_price

#Final bill
print(f"Your final bill is: ${bill} ")
