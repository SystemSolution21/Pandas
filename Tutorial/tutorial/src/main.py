import os
import sys
import pandas as pd

# Pandas Series
print("-----Pandas Series-----")
ser_lst: list = [1, 3, 2]
df = pd.Series(ser_lst)
print(df)

print("# Create Labels for Series")
ser_lbl: list = ["x", "y", "z"]
ser_lst_lbl = pd.Series(ser_lst, index = ser_lbl)
print(ser_lst_lbl)
print(ser_lst_lbl["y"])

print("# Pandas Series Dictionary")
calories = pd.Series({"day1": 420, "day2": 380, "day3": 390,})
print(calories)

print("# Create Series using index argument to specify the desire items")
print(pd.Series(calories, index=["day2", "day3"]))

# Pandas DataFrame
print("-----Pandas DataFrame-----")
data_dict: dict = {"calories":[420, 380, 390],
              "duration":[50, 40, 45]}
df = pd.DataFrame(data_dict)
print(df)

print("# Refer to row index")
print(df.loc[0])

print("# Using list index return Pandas Series")
print(df.loc[[0, 1]])

# Get current directory
print("-----Get current directory-----")
current_dir: str = os.path.dirname(__file__)
print(current_dir)

# Construct relative path to the csv file
csv_file = os.path.join(current_dir, "..", "data", "data.csv")

# Pandas read csv file
print("-----Pandas read csv file-----")
data = pd.read_csv(csv_file)
print(data.head())
