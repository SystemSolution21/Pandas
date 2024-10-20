import os
from numpy import float64
import pandas as pd

print("#Read csv data file")
dir_name: str = os.path.dirname(__file__)
file: str = os.path.join(dir_name, "..", "data", "clean.csv")
df: pd.DataFrame = pd.read_csv(file, header=0, sep=",")
print(df.to_string()) #Show all data
print(df.info()) #Data catagories information
print(df.describe()) #Describe data statistics

print("#Cleaning Nan/Null data")
#Note: df.dropna(inplace=True) will permanently remove data from original DataFrame
clean_na_df: pd.DataFrame = df.dropna()
print(clean_na_df.to_string())

print("#Fill data to specific Column")
fill_na_df: pd.DataFrame = df.copy()
fill_na_df.fillna({"Calories": 130}, inplace=True)
print(fill_na_df.to_string())

print("#Fill data using mean()")
fill_na_df = df.copy()
mean_calories: float = fill_na_df["Calories"].mean()
fill_na_df.fillna({"Calories": mean_calories}, inplace = True)
print(fill_na_df.to_string())

print("#Fill data using median()")
fill_na_df = df.copy()
median_calories: float = fill_na_df["Calories"].median()
fill_na_df.fillna({"Calories": median_calories}, inplace = True)
print(fill_na_df.to_string())

print("#Fill data using mode()")
fill_na_df = df.copy()
mode_calories: float = fill_na_df["Calories"].mode()[0]
fill_na_df.fillna({"Calories": mode_calories}, inplace = True)
print(fill_na_df.to_string())

print("#Convert type int64 ot float64 for Data Preparation")
print(df.info())
df["Pulse"] = df["Pulse"].astype(float64)
df["Maxpulse"] = df["Maxpulse"].astype(float64)
print(df.info())
