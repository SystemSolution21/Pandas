import os
import pandas as pd

#Read csv data file
path: str = os.path.dirname(__file__)
file: str = os.path.join(path, "..", "data", "clean.csv")
df: pd.DataFrame = pd.read_csv(file)

#Cleaning Nan/Null data
#Note: df.dropna(inplace=True) will permanently remove data from original DataFrame
clean_na_df = df.dropna()
print(clean_na_df.to_string())

#Fill data to specific Column
fill_na_df = df.copy()
fill_na_df["Calories"].fillna(130, inplace = True)
print(fill_na_df.to_string())

#Fill data using mean()
fill_na_df = df.copy()
mean_calories = fill_na_df["Calories"].mean()
fill_na_df["Calories"].fillna(mean_calories, inplace = True)
print(fill_na_df.to_string())

#Fill data using median()
fill_na_df = df.copy()
median_calories = fill_na_df["Calories"].median()
fill_na_df["Calories"].fillna(median_calories, inplace = True)
print(fill_na_df.to_string())

#Fill data using mode()
fill_na_df = df.copy()
mode_calories = fill_na_df["Calories"].mode()[0]
fill_na_df["Calories"].fillna(mode_calories, inplace = True)
print(fill_na_df.to_string())
