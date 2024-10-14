import os
import pandas as pd

def main():        

    # Pandas DataFrame
    print("# Pandas DataFrame")
    data_dict: dict[str, list[int]] = {"calories":[420, 380, 390],
                        "duration":[50, 40, 45]}
    df: pd.DataFrame = pd.DataFrame(data_dict)
    print(df)

    print("# Add index range")
    index_range: pd.RangeIndex = pd.RangeIndex(start=1, stop=len(df)+1, step=1)
    df.index = index_range
    print(df)

    print("# Locate row data using loc[]")
    print(df.loc[1])

    print("# Locate index list to return Pandas Series")
    print(df.loc[[2, 3]])
    
    print("# Add index date range")
    date_range: pd.DatetimeIndex = pd.date_range(start="2024-10-14", periods=len(df), freq='D')
    df.index = date_range
    print(df)

    print("# Add custom index")
    custom_index: pd.Index = pd.Index([f'Day{i+1}' for i in range(len(df))])
    df.index = custom_index
    print(df)


if __name__ == "__main__":
    main()
