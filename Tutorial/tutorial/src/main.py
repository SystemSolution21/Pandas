import os
import sys
import pandas as pd

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
