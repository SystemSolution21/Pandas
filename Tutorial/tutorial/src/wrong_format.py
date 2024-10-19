import os
import pandas as pd

#Read csv file
dir_name: str = os.path.dirname(__file__)
file: str= os.path.join(dir_name, "..", "data", "clean.csv")
df: pd.DataFrame = pd.read_csv(file)
print(df.to_string())

#Cleaning wrong data format 
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
print(df.to_string())
