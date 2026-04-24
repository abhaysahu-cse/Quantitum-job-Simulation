import pandas as pd
import os

# --- Load all three CSV files ---
data_files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv",
]

frames = [pd.read_csv(f) for f in data_files]
df = pd.concat(frames, ignore_index=True)

print(f"Total rows loaded: {len(df)}")

# --- Filter: keep only Pink Morsels ---
df = df[df["product"] == "pink morsel"]
print(f"Rows after filtering for 'pink morsel': {len(df)}")

# --- Clean price column: strip the '$' and convert to float ---
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

# --- Calculate sales = quantity * price ---
df["sales"] = df["quantity"] * df["price"]

# --- Keep only the required output columns ---
output = df[["sales", "date", "region"]]

# --- Write to output CSV ---
os.makedirs("output", exist_ok=True)
output_path = "output/processed_sales.csv"
output.to_csv(output_path, index=False)

print(f"Output written to: {output_path}")
print(f"Output rows: {len(output)}")
print("\nSample output:")
print(output.head(10).to_string(index=False))
