import os
import pandas as pd

def main() -> None:        
    
    print("#Create Pandas Series")
    list_series: list[int] = [1, 3, 2]
    ps: pd.Series = pd.Series(list_series)
    print(ps)

    print("#Add index labels")
    index_label: pd.Index = pd.Index(["x", "y", "z"])
    ps.index = index_label
    print(ps)
    print("# 'Y' index data")
    print(ps["y"])

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