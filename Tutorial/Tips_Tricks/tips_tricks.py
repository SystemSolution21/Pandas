import numpy as np
import pandas as pd

# 1. Merging with the Indicator Argument
df1 = pd.DataFrame(data={"key": ["A", "B", "C"], "value": [1, 2, 3]})
df2 = pd.DataFrame(data={"key": ["B", "C", "D"], "value": [4, 5, 6]})

merged: pd.DataFrame = pd.merge(
    left=df1, right=df2, on="key", how="outer", indicator=True
)

print(merged)


# 2. Custom chaining with pipe
df: pd.DataFrame = pd.DataFrame(
    data={
        "Quantity": [10, 15, 10, 20],
        "Price": [100, 150, 200, 250],
    }
)


def calc_total(df) -> pd.DataFrame:
    df["Total"] = df["Quantity"] * df["Price"]
    return df


result: pd.DataFrame = (
    df.pipe(func=calc_total)
    .query(expr="Total > 1000")
    .sort_values(by="Total", ascending=False)
)

# Sorting index
index_range: pd.RangeIndex = pd.RangeIndex(start=1, stop=len(result) + 1, step=1)
result.index = index_range
print(result)

price = np.arange(100, 250, step=50, dtype=np.int32)
print(price)

# 3. Identify Duplicates and Drop Duplicates
df = pd.DataFrame(
    data={
        "ID": [1, 2, 2, 3, 4, 4],
        "Name": ["Alice", "Bob", "Bob", "Charlie", "David", "David"],
    }
)
print(df)

duplicated: pd.DataFrame = df[df.duplicated(subset="ID", keep=False)]
print(duplicated)

drop_duplicates: pd.DataFrame = df.drop_duplicates(subset="ID")
print(drop_duplicates)

# 4. Binning Data with cut and qcut
data: dict[str, list[int]] = {
    "Age": [22, 25, 29, 34, 45, 52, 61, 70, 80, 90],
    "Income": [25000, 27000, 30000, 32000, 40000, 50000, 60000, 70000, 80000, 90000],
}
df = pd.DataFrame(data=data)
print(df)

# Equal-width binning for Age
age_bins: list[int] = [0, 18, 35, 60, 100]
age_labels: list[str] = ["Child", "Young Adult", "Adult", "Senior"]
df["Age Group"] = pd.cut(x=df["Age"], bins=age_bins, labels=age_labels)
print(df)

# Quantile-based binning for Income
df["Income Quartile"] = pd.qcut(df["Income"], 4, labels=["Q1", "Q2", "Q3", "Q4"])
print(df)

# 5. Interpolating Data
df: pd.DataFrame = pd.DataFrame(
    data={
        "Date": pd.date_range(start="1/1/2024", periods=5, freq="D"),
        "Value": [1, np.nan, np.nan, 4, 5],
    }
)
print(df)

df["Interpolated"] = df["Value"].interpolate(method="linear")
print(df)
