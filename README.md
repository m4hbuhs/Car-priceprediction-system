# Car Price Prediction System

An end-to-end Machine Learning project that predicts the selling price of used cars based on vehicle details such as car model, manufacturing year, fuel type, transmission type, ownership history, and kilometers driven.

---

## Project Overview

Determining the fair value of a used car can be difficult due to multiple influencing factors. This project uses Machine Learning to estimate the selling price of a vehicle based on historical car sales data.

The project covers the complete ML workflow:

* Data Cleaning
* Feature Engineering
* Model Training
* Hyperparameter Tuning
* Model Evaluation
* Model Serialization
* Streamlit Deployment

---

## Dataset Information

### Features Used

| Feature      | Description               |
| ------------ | ------------------------- |
| Car_Name     | Vehicle Model Name        |
| Year         | Manufacturing Year        |
| Kms_Driven   | Total Kilometers Driven   |
| Fuel_Type    | Petrol / Diesel / CNG     |
| Seller_Type  | Dealer / Individual       |
| Transmission | Manual / Automatic        |
| Owner        | Number of Previous Owners |

### Target Variable

| Column        | Description               |
| ------------- | ------------------------- |
| Selling_Price | Car Selling Price (Lakhs) |

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Matplotlib
* Streamlit
* Pickle

---

## Machine Learning Pipeline

### Data Preprocessing

* Handling categorical variables using One-Hot Encoding
* Feature transformation using ColumnTransformer
* Train-Test Split
* Scikit-Learn Pipeline implementation
* Prevention of Data Leakage

### Models Evaluated

1. Linear Regression (Baseline)
2. Random Forest Regressor
3. XGBoost Regressor

---

## Model Performance

| Model             | MAE      | RMSE     | R² Score  |
| ----------------- | -------- | -------- | --------- |
| Linear Regression | 1.30     | 1.92     | 0.839     |
| Random Forest     | 1.11     | 1.77     | 0.863     |
| XGBoost           | **0.84** | **1.32** | **0.924** |

### Best Model
 XGBoost Regressor

Performance:

* Mean Absolute Error (MAE): **0.84**
* Root Mean Squared Error (RMSE): **1.32**
* R² Score: **92.4%**

The XGBoost model achieved the highest predictive performance and was selected for deployment.

---

## Streamlit Application

The project includes an interactive Streamlit application where users can:

* Select vehicle model
* Choose fuel type
* Select transmission type
* Enter kilometers driven
* Select ownership information
* Predict selling price instantly

Run the application locally:

```bash
streamlit run app.py
```

---

## Project Structure

```text
Car-priceprediction-system/
│
├── app.py
├── car_prediction_data.csv
├── Car_price_model.pkl
├── car_price_prediction.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/m4hbuhs/Car-priceprediction-system.git
```

Move into the project directory:

```bash
cd Car-priceprediction-system
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

---

## Screenshots

Add screenshots of:

* Streamlit Home Page
* Prediction Results
* Model Evaluation Graphs

---

## Future Improvements

* Deploy on Streamlit Cloud
* Add Feature Importance Dashboard
* Improve Hyperparameter Optimization
* Add More Vehicle Features
* Collect Larger Dataset

---

##  Author

**Shubham**

GitHub: https://github.com/m4hbuhs

---

⭐ If you found this project useful, consider giving the repository a star.
