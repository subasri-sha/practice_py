# DataFrame

import pandas as pd

# name= [' John', 'Nike', 'Alex']

# result = pd.DataFrame(name)
# print(result)

# Dictionary Data Type

student = {
    "Name": ['Suba', 'Abi', 'Alex', 'Harris', 'Rahman'],
    "Score": [50, 45, 39, 45, 50]
}

result = pd.DataFrame(student)
print(result)
