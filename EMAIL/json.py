import json
import csv
import pandas as pd

# -------------------------------
# Load JSON File
# -------------------------------
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# -------------------------------
# Convert JSON to CSV
# -------------------------------
def json_to_csv(json_data, csv_file):
    keys = json_data[0].keys()

    with open(csv_file, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(json_data)

    print(f"CSV file '{csv_file}' created successfully!")


# -------------------------------
# HEAD function (like pandas)
# -------------------------------
def head(data, n=5):
    print("\n--- HEAD ---")
    for i, row in enumerate(data[:n]):
        print(row)


# -------------------------------
# INFO function (like pandas)
# -------------------------------
def info(data):
    print("\n--- INFO ---")
    total_rows = len(data)
    print(f"Total Rows: {total_rows}")

    for key in data[0].keys():
        dtype = type(data[0][key]).__name__
        print(f"{key} -> {dtype}")


# -------------------------------
# DESCRIBE function (basic version)
# -------------------------------
def describe(data):
    print("\n--- DESCRIBE ---")

    numeric_cols = {}

    # Extract numeric columns
    for key in data[0].keys():
        values = [row[key] for row in data if isinstance(row[key], (int, float))]
        if values:
            numeric_cols[key] = values

    for col, values in numeric_cols.items():
        count = len(values)
        mean = sum(values) / count
        minimum = min(values)
        maximum = max(values)

        print(f"\nColumn: {col}")
        print(f"Count: {count}")
        print(f"Mean: {mean}")
        print(f"Min: {minimum}")
        print(f"Max: {maximum}")


# -------------------------------
# MAIN FUNCTION
# -------------------------------
def main():
    json_file = "data.json"
    csv_file = "output.csv"

    # Load JSON
    data = load_json(json_file)

    # Convert to CSV
    json_to_csv(data, csv_file)

    # Custom Functions
    head(data)
    info(data)
    describe(data)

    # -------------------------------
    # Using Pandas (for comparison)
    # -------------------------------
    print("\n\n--- USING PANDAS ---")
    df = pd.read_json(json_file)

    print("\nHEAD:")
    print(df.head())

    print("\nINFO:")
    print(df.info())

    print("\nDESCRIBE:")
    print(df.describe())


# Run the program
if __name__ == "__main__":
    main()