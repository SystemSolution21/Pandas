import os
import pandas as pd

def main():

    print("# Get current directory")
    current_dir: str = os.path.dirname(__file__)
    print(current_dir)

    print("# Construct relative path to the csv file")
    csv_file = os.path.join(current_dir, "..", "data", "data.csv")
    print(csv_file)

    # Pandas read csv file
    print("-----Pandas read csv file-----")
    data = pd.read_csv(csv_file)
    print(data.to_string())

if __name__ == "__name__":
    main()
