#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
# password = " "  # empty password variable

# if nr_letters < 0 or nr_symbols < 0 or nr_numbers < 0:  # check for negative input
#     print("Please enter a valid number") 
 
# for char in range(0, nr_letters):  # loop to add letters to generate password
#     password += random.choice(letters)  # add random letter from the list to "password"

# for char in range(0, nr_symbols): # loop to add symbols to generate password
#     password += random.choice(symbols) # add random symbol frim the list to "password"

# for char in range(0, nr_numbers): # loop to add numbers to generate password
#     password += random.choice(numbers) # add random number from the list to "password"

# print(password) #print the generated password


# Hard level - Order of characters randomised:

password_list = [ ] # empty list to store the password characters

for char in range(0, nr_letters):  # loop to add letters to generate password
    password_list += random.choice(letters)  # add random letter from the list to "password_list"

for char in range(0, nr_symbols): # loop to add symbols to generate password
    password_list += random.choice(symbols) # add random symbol frim the list to "password_list"

for char in range(0, nr_numbers): # loop to add numbers to generate password
    password_list += random.choice(numbers) # add random number from the list to "password_list"

random.shuffle(password_list) #shuffle the password list to randomise the order of characters

# print(password_list) #print the password list

# To store the final password as a string

password = " " #empty password variable to store the final password

for char in password_list:
    password += char #add each character from the password list to the password variable

print(f"Your password is: {password}") #print the final password
