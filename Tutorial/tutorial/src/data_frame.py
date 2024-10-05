import os
import pandas as pd

def main():        

    # Pandas DataFrame
    print("-----Pandas DataFrame-----")
    data_dict: dict = {"calories":[420, 380, 390],
                "duration":[50, 40, 45]}
    df = pd.DataFrame(data_dict)
    print(df)

    print("# Using .loc[] to refer row index")
    print(df.loc[0])

    print("# Using list index, return Pandas Series")
    print(df.loc[[0, 1]])

    print("# Add list names to give each row name")
    row_names: list[str] = ["day1", "day2", "day3"]
    df = pd.DataFrame(data_dict, index=row_names)
    print(df)

if __name__ == "__main__":
    main()
