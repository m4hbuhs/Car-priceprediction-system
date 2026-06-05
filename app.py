import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Car Price Predictor")

# Load model
with open("car_price_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title(" Car Price Predictor")

# Car Names from dataset
car_name = st.selectbox(
    "Car Name",
    sorted([
        'ritz','sx4','ciaz','wagon r','swift','vitara brezza',
        's cross','alto 800','ertiga','dzire','alto k10','ignis',
        '800','baleno','omni','fortuner','innova','corolla altis',
        'etios cross','etios g','etios liva','corolla','etios gd',
        'camry','land cruiser','Royal Enfield Thunder 500',
        'UM Renegade Mojave','KTM RC200','Bajaj Dominar 400',
        'Royal Enfield Classic 350','KTM RC390',
        'Hyosung GT250R','Royal Enfield Thunder 350',
        'KTM 390 Duke ','Mahindra Mojo XT300',
        'Bajaj Pulsar RS200','Royal Enfield Bullet 350',
        'Royal Enfield Classic 500','Bajaj Avenger 220',
        'Bajaj Avenger 150','Honda CB Hornet 160R',
        'Yamaha FZ S V 2.0','Yamaha FZ 16',
        'TVS Apache RTR 160','Bajaj Pulsar 150',
        'Honda CBR 150','Hero Extreme',
        'Bajaj Avenger 220 dtsi','xcent','elantra',
        'creta','verna','city','brio','amaze','jazz'
    ])
)

year = st.slider(
    "Manufacturing Year",
    min_value=2000,
    max_value=2025,
    value=2018
)

kms_driven = st.slider(
    "Kilometers Driven",
    min_value=0,
    max_value=300000,
    value=25000,
    step=1000
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Dealer", "Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Owner",
    [0, 1, 2, 3]
)

if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "Car_Name": [car_name],
        "Year": [year],
        "Kms_Driven": [kms_driven],
        "Fuel_Type": [fuel_type],
        "Seller_Type": [seller_type],
        "Transmission": [transmission],
        "Owner": [owner]
    })

    prediction = model.predict(input_df)

    st.success(
        f"Estimated Selling Price: ₹ {prediction[0]:.2f} Lakhs"
    )