# Convert "Data" into a tuple of characters without using tuple() function

name = "Data"
result = () # empty tuple
for char in name: 
    result += char, # adding , to make it a tuple
print(result)