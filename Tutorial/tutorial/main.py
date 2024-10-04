import os
import pandas as pd

# Get current working directory
path: str = os.getcwd()
print(path)

# Pandas DataFrame
df = pd.DataFrame({"A": [1, 2, 3, 4, 5]})
print(df)

