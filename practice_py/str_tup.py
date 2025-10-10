# Convert "Data" into a tuple of characters without using tuple() function

name = "Data"
result = () # empty tuple
for char in name: 
    result += char, # adding , to make it a tuple
print(result)

# # Given name = "Python", print each character on a new line
name = "Python"

for char in name:
    print(char)

