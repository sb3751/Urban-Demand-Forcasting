import pandas as pd

# Load raw transport data
df = pd.read_csv("data/raw/transport_ridership_monthly_raw.csv")

# Convert Month column to datetime
df["Month"] = pd.to_datetime(df["Month"], format="%m/%d/%Y")

# Extract year and month
df["year"] = df["Month"].dt.year
df["month"] = df["Month"].dt.month

# Group by year and month, sum ridership across agencies
monthly_transport = (
    df.groupby(["year", "month"], as_index=False)["Ridership"]
      .sum()
      .rename(columns={"Ridership": "total_ridership"})
)

# Check result
print(monthly_transport.head())
print(monthly_transport.info())

# Save cleaned data
monthly_transport.to_csv(
    "data/processed/transport_ridership_monthly_clean.csv",
    index=False
)
