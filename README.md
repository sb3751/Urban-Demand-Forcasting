# 🏙️ Urban Demand Forecasting System

## 📌 Overview
This project presents an end-to-end **Urban Demand Forecasting System** that predicts future demand patterns using historical **public transport ridership** and **electricity consumption** data.  
The system is designed to support **urban planning, infrastructure management, and smart city research** by providing interpretable and statistically sound demand forecasts.

The project emphasizes:
- Time-series formulation of real-world problems  
- Model interpretability over black-box accuracy  
- Robust validation under real-world structural shocks (e.g., COVID-19)

---

## 📊 Datasets
The system operates on two independent urban demand domains:

### 1️⃣ Transport Demand (Monthly)
- Public transport ridership data
- Exhibits strong seasonality and long-term trends
- Contains a major structural break during the COVID-19 period

### 2️⃣ Energy Demand (Yearly)
- Electricity consumption data
- Captures long-term demand growth trends
- Minimal seasonality at yearly resolution

---

## 🧱 Project Pipeline
```

Raw Data
↓
Data Cleaning & Processing
↓
Time-Series Modeling
↓
Forecast Generation
↓
Visualization & Evaluation

````

Each stage is modular and reproducible.

---

## 🧠 Methodology

### Problem Formulation
Urban demand forecasting is inherently a **time-series problem**, where future demand depends on historical patterns observed over time.  
The datasets used in this project are sequential, time-ordered, and exhibit trend and seasonal behavior, making statistical time-series models the most suitable choice.

---

### Model Selection Rationale
- **SARIMA (Seasonal ARIMA)** was used for transport demand to capture:
  - Monthly seasonality
  - Autocorrelation
  - Long-term trends
- **ARIMA (Non-seasonal)** was used for energy demand due to:
  - Yearly data resolution
  - Dominant long-term trend
  - Absence of short-term seasonality

---

### Why Not Machine Learning?
Machine learning and deep learning models were not used because:
- They do not naturally capture temporal dependency without heavy feature engineering
- Dataset sizes are moderate, increasing the risk of overfitting
- Interpretability is critical for urban planning and policy contexts

Statistical models such as ARIMA provide **transparent, explainable forecasts**, which are preferred in infrastructure and research-driven applications.

---

## 🔍 Assumptions

### Transport Demand
- Monthly ridership follows recurring seasonal patterns
- Historical trends influence future demand
- COVID-19 represents a **structural shock**, not a permanent pattern

### Energy Demand
- Electricity demand follows a long-term trend
- Yearly aggregation smooths short-term fluctuations
- External shocks are less pronounced at yearly resolution

---

## ⚠️ Limitations
- ARIMA-based models assume future behavior resembles historical patterns
- Unprecedented events (pandemics, policy shifts) reduce accuracy
- Models are currently **univariate** and do not include exogenous variables such as population, weather, or economic indicators

---

## 📏 Validation Strategy

### Time-Aware Holdout Validation
Random train–test splits are inappropriate for time-series data due to data leakage.  
This project adopts a **time-aware validation strategy**, training on historical data and testing on future observations.

---

### Transport Validation
- Training data: Pre-2020
- Testing data: COVID + recovery period
- Evaluation metrics:
  - **MAE (Mean Absolute Error)**
  - **RMSE (Root Mean Squared Error)**

Higher errors during COVID are expected and reflect model limitations under extreme shocks rather than modeling failure.

---

### Energy Validation
Due to limited yearly observations, validation focuses on:
- Residual diagnostics
- Long-term trend stability
- Interpretability of forecasts rather than short-term accuracy

---

## 🔁 Rolling (Walk-Forward) Validation
To further assess robustness, **rolling validation** was applied to transport demand forecasting:
- Model trained on an initial window
- Forecasts one month ahead
- Training window expanded iteratively

This simulates **real-world operational forecasting**, where models are updated as new data becomes available.

---

## 📈 Results
- Transport demand forecasts reveal the impact of COVID as a structural break
- SARIMA produces a counterfactual “no-COVID” projection, highlighting interpretability
- Energy demand forecasts provide stable 5-year long-term projections
- Rolling validation confirms model stability under evolving conditions

All results include **historical vs predicted visualizations** for interpretability.

---

## ▶️ How to Run

From the project root directory:

```bash
python notebooks/transport_forecasting.py
python notebooks/energy_forecasting.py
````

Generated plots are saved automatically for reporting and presentation.

---

## 🔮 Capabilities & Extensions

The system can be extended to:

* Water demand forecasting
* Traffic congestion analysis
* Housing or population demand modeling
* Multivariate forecasting using **SARIMAX**
* Policy scenario simulation

---

# 🧱 Project Architecture (How It Is Built)

Think of the project as **5 layers**:

```
Raw Data
   ↓
Data Cleaning
   ↓
Time-Series Modeling
   ↓
Forecast Generation
   ↓
Visualization & Interpretation

## 🏁 Conclusion

This project demonstrates how **interpretable statistical time-series models** can be effectively used for urban demand forecasting.
By combining rigorous methodology, honest validation, and clear limitations, the system is well-suited for **graduate research, smart city studies, and data-driven infrastructure planning**.

---

## 🎓 Author

**Sanidhya Bhagat**
Urban Demand Forecasting Project

```

---

## ✅ What This README Achieves
- ✔ Academically defensible  
- ✔ Interview-ready  
- ✔ Admission-ready (Japan / research-focused programs)  
- ✔ Clean and professional GitHub presentation  
