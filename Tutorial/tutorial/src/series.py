import os
import pandas as pd

def main() -> None:        
    
    print("#Create Pandas Series")
    list_series: list[int] = [1, 3, 2]
    ds: pd.Series = pd.Series(list_series)
    print(ds)

    print("#Add index labels")
    index_label: list[str] = ["x", "y", "z"]
    ds: pd.Series = pd.Series(list_series, index = index_label)
    print(ds)
    print("# 'Y' index data")
    print(ds["y"])

    print("#Create Pandas Series using Dictionary")
    dict_data: dict[str, int] = {"day1": 420,
                                  "day2": 380,
                                    "day3": 390,}
    dict_series: pd.Series = pd.Series(dict_data)
    print(dict_series)

    print("#Create new Series using specific index list of items")
    new_ps: pd.Series = pd.Series(dict_series, index=["day2", "day3"])
    print(new_ps)


if __name__ == "__main__":
    main() 