import os
from typing import Any
import pandas as pd
from datetime import date

def main() -> None:
    # Ger current directory
    path: str = os.path.dirname(__file__)
    json_file: str = os.path.join(path, "..", "data", "data.json")
    print("# Read json file")
    df: pd.DataFrame = pd.read_json(json_file)
    print(df.to_string())

    print("# Add date range index")
    date_index: pd.DatetimeIndex= pd.date_range(date.today(), periods=len(df), freq='D')
    df.index = date_index
    print(df.to_string())


if __name__ == "__main__":
    main()

