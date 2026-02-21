import pandas as pd

# Load raw energy data
df = pd.read_csv("data/raw/energy_consumption_monthly_raw.csv")

# Filter for United States
usa_energy = df[df["country"] == "United States"]

# Keep only year and electricity demand
usa_energy = usa_energy[["year", "electricity_demand"]]

# Drop missing values
usa_energy = usa_energy.dropna()

# Sort by year
usa_energy = usa_energy.sort_values("year")

# Check result
print(usa_energy.head())
print(usa_energy.info())

# Save cleaned energy data
usa_energy.to_csv(
    "data/processed/energy_demand_yearly_clean.csv",
    index=False
)
