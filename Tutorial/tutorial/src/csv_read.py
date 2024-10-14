import os
import pandas as pd
from datetime import date

def main()-> None:

    print("# Get current directory")
    current_dir: str = os.path.dirname(__file__)
    print(current_dir)

    print("# Construct relative path to the csv file")
    csv_file: str = os.path.join(current_dir, "..", "data", "data.csv")
    print(csv_file)

    print("# Pandas read csv file")
    df: pd.DataFrame = pd.read_csv(csv_file)
    print(df.to_string())

    print("# Default head data")
    print(df.head())

    print("# Display first 10 data")
    print(df.head(10))

    print("# Default tail data")
    print(df.tail())

    print("# Check number of returned rows")
    print(pd.options.display.max_rows)

    print("# Default head and tail data")
    print(df.to_string)

    print("# Add date index")
    date_index: pd.DatetimeIndex = pd.date_range(start=date.today(), periods=len(df), freq='D' )
    df.index = date_index
    print(df.to_string())

    print("# Data information")
    print(df.info())

    print("# Describe data statistic")
    print(df.describe())


if __name__ == "__main__":
    main()
