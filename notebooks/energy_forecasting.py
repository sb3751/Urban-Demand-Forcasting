import pandas as pd
import matplotlib.pyplot as plt
from pmdarima import auto_arima

# Load clean energy data
df = pd.read_csv("data/processed/energy_demand_yearly_clean.csv")

# Convert year to datetime index
df["year"] = pd.to_datetime(df["year"], format="%Y")
df.set_index("year", inplace=True)

# Fit Auto ARIMA (non-seasonal, yearly data)
model = auto_arima(
    df["electricity_demand"],
    seasonal=False,
    stepwise=True,
    suppress_warnings=True
)

print(model.summary())

# Forecast next 5 years
n_future = 5
forecast = model.predict(n_periods=n_future)

# Create future year index
last_year = df.index.max()
future_years = pd.date_range(
    start=last_year + pd.DateOffset(years=1),
    periods=n_future,
    freq="YS"
)

forecast_series = pd.Series(forecast, index=future_years)

# Plot historical + forecast
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["electricity_demand"], label="Historical Demand")
plt.plot(forecast_series.index, forecast_series, label="5-Year Forecast", linestyle="--")
plt.title("5-Year Forecast of Electricity Demand")
plt.xlabel("Year")
plt.ylabel("Electricity Demand")
plt.legend()
plt.tight_layout()

# Save and show plot
plt.savefig("energy_demand_5_year_forecast.png")
plt.show()
