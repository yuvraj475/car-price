import pandas as pd 
import numpy as np 
import streamlit as st 




st.set_page_config(
    page_title="Used Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Used Car Price Predictor")
st.write("Streamlit app is working!")

df = pd.read_csv("cardekho_dataset.csv")
st.markdown("### 🚘 Car Information")
st.caption("Enter the details of the car to estimate its selling price.")

col1, col2 = st.columns(2)

with col1:
    car_brand = st.selectbox(
        "🏷️ Select Your Car Brand",
        df["brand"].unique()
    )

with col2:
    model = st.selectbox(
        "🚘 Select Car Model",
        (df[df["brand"] == car_brand])["model"].unique()
    )


col1, col2 = st.columns(2)

with col1:
    age_of_vehicle = st.number_input(
        "📅 Vehicle Age",
        min_value=0,
        step=1
    )

with col2:
    kms_driven = st.number_input(
        "🛣️ KMs Driven",
        min_value=0,
        step=100
    )


# 👇 YE NAYA ROW hai — previous with col2 ke bahar
col1, col2 = st.columns(2)

with col1:
    fuel_type = st.selectbox(
        "⛽ Fuel Type",
        df["fuel_type"].unique()
    )

with col2:
    transmission = st.selectbox(
        "⚙️ Transmission",
        df["transmission_type"].unique()
    )



col1,col2=st.columns(2)
with col1:
    seller_type= st.selectbox('🔧 Seller Type',df['seller_type'].unique())

    with col2:
        engine = st.number_input('👤 engine CC',min_value=0)


col1,col2 = st.columns(2)

with col1:
    max_power = st.number_input('⚡MAx Power(BHP)',min_value=0)
    with col2:
        seats=st.number_input('💺Seat',min_value=0)

import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "car_price_tuned_x_pipeline.pkl")

model = joblib.load(model_path)


input_data = pd.DataFrame({
'brand':[car_brand],
'model':[model],
'vehicle_age':[age_of_vehicle],
'km_driven':[kms_driven],
'seller_type':[seller_type],
'fuel_type':[fuel_type],
'transmission_type':[transmission],
'engine':[engine],
'max_power':[max_power],
'seats':[seats]
})

st.markdown("---")
if st.button("🔮 Predict Selling Price", use_container_width=True):

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Selling Price: ₹{prediction:,.0f}")

    
