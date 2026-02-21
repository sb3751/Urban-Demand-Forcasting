import pandas as pd
import matplotlib.pyplot as plt
from pmdarima import auto_arima
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load clean transport data
df = pd.read_csv("data/processed/transport_ridership_monthly_clean.csv")

# Create datetime index
df["date"] = pd.to_datetime(
    df["year"].astype(str) + "-" + df["month"].astype(str) + "-01"
)
df = df.sort_values("date")
df.set_index("date", inplace=True)

# Train-test split
train = df[df.index < "2020-01-01"]
test = df[df.index >= "2020-01-01"]

# Fit SARIMA model
model = auto_arima(
    train["total_ridership"],
    seasonal=True,
    m=12,
    stepwise=True,
    suppress_warnings=True
)

# Forecast for test period
forecast = model.predict(n_periods=len(test))

# Accuracy metrics
mae = mean_absolute_error(test["total_ridership"], forecast)
rmse = np.sqrt(mean_squared_error(test["total_ridership"], forecast))

print(f"MAE  : {mae:,.0f}")
print(f"RMSE : {rmse:,.0f}")

# Plot actual vs forecast
plt.figure(figsize=(10, 5))
plt.plot(test.index, test["total_ridership"], label="Actual")
plt.plot(test.index, forecast, label="Forecast", linestyle="--")
plt.title("SARIMA Forecast vs Actual (COVID + Recovery)")
plt.xlabel("Year")
plt.ylabel("Total Ridership")
plt.legend()
plt.tight_layout()
plt.show()

# -------------------------------
# Rolling (Walk-Forward) Validation
# -------------------------------

from sklearn.metrics import mean_squared_error
import numpy as np

rolling_predictions = []
rolling_actuals = []

# Initial training window (pre-COVID)
rolling_train = df[df.index < "2020-01-01"]["total_ridership"]

for date in test.index:
    model = auto_arima(
        rolling_train,
        seasonal=True,
        m=12,
        stepwise=True,
        suppress_warnings=True
    )
    
    pred = model.predict(n_periods=1).iloc[0]
    actual = df.loc[date, "total_ridership"]
    
    rolling_predictions.append(pred)
    rolling_actuals.append(actual)
    
    # Expand training window
    rolling_train = pd.concat(
        [rolling_train, pd.Series([actual], index=[date])]
    )

# Rolling RMSE
rolling_rmse = np.sqrt(
    mean_squared_error(rolling_actuals, rolling_predictions)
)

print(f"Rolling RMSE: {rolling_rmse:,.0f}")
