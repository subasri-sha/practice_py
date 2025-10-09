# Read csv file using pandas

import pandas as pd

df = pd.read_csv("C:\\Users\\subas\\OneDrive\\pynotes.a\\people_data.csv")
print(df) # print entire data frame
print(df.head(10)) # print first 10 rows
print(df.tail(10)) # print last 10 rows

# Filtering data

print(df[df["Name"] == "Daniel Johnson"]) # filter data where Name is Daniel Johnson
print(df[df["Age"] > 30]) # filter data where Age is greater than 30