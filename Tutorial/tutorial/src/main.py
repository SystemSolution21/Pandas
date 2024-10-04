import os
import sys
import pandas as pd

print("-------------------------------------------------------------------------------------")
# Pandas Series
print("Pandas Series")
ser_lst: list = [1, 3, 2]
df = pd.Series(ser_lst)
print(df)

# Create Labels for Series
print("Create Labels for Series")
ser_lbl: list = ["x", "y", "z"]
ser_lst_lbl = pd.Series(ser_lst, index = ser_lbl)
print(ser_lst_lbl)
print("-------------------------------------------------------------------------------------")

print("-------------------------------------------------------------------------------------")
# Pandas DataFrame
print("Pandas DataFrame")
df = pd.DataFrame({"A": [1, 2, 3, 4, 5]})
print(df)
print("-------------------------------------------------------------------------------------")

# Get current directory
current_dir: str = os.path.dirname(__file__)
print(current_dir)

# Construct relative path to the csv file
csv_file = os.path.join(current_dir, "..", "data", "data.csv")

# Pandas read csv file
print("Pandas read csv file")
data = pd.read_csv(csv_file)
print(data.head())
print("-------------------------------------------------------------------------------------")