import streamlit as st
import numpy as np
import joblib  # for loading saved model

# Load your trained model
best_model = joblib.load("model.pkl")  # Replace with your model file name

def predict_tomorrow_open(open_price, high_price, low_price, close_price):
    input_data = np.array([[open_price, high_price, low_price, close_price]])
    prediction = best_model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.set_page_config(page_title="AdaniENT Open Price Predictor")
st.title("📈 AdaniENT Open Price Predictor")
st.write("Enter today's Open, High, Low, and Close prices to predict tomorrow's opening price.")

# Input fields
open_price = st.number_input("Today’s Open Price", format="%.2f")
high_price = st.number_input("Today’s High Price", format="%.2f")
low_price = st.number_input("Today’s Low Price", format="%.2f")
close_price = st.number_input("Today’s Close Price", format="%.2f")

# Predict button
if st.button("Predict"):
    result = predict_tomorrow_open(open_price, high_price, low_price, close_price)
    st.success(f"📊 Predicted Tomorrow's Open Price: ₹{result:.2f}")

#streamlit run app.py