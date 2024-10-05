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

if __name__ == "__main__":
    main()
