import os
import pandas as pd

def main():        
    
    # Pandas Series
    print("-----Pandas Series-----")
    ser_lst: list = [1, 3, 2]
    df = pd.Series(ser_lst)
    print(df)

    print("# Create Labels for Series using index= argument")
    ser_lbl: list = ["x", "y", "z"]
    ser_lst_lbl = pd.Series(ser_lst, index = ser_lbl)
    print(ser_lst_lbl)
    print(ser_lst_lbl["y"])

    print("# Pandas Series Dictionary")
    calories = pd.Series({"day1": 420, "day2": 380, "day3": 390,})
    print(calories)

    print("# Create Series using index= argument to specify the desire items")
    print(pd.Series(calories, index=["day2", "day3"]))

if __name__ == "__name__":
    main()