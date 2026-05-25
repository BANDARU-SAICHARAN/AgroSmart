import streamlit as st
import pickle
import numpy as np


st.set_page_config(
    page_title="AgroSmart AI",
    page_icon="🌾"
)


model = pickle.load(open('Model/crop_model.pkl', 'rb'))


st.title("🌾 AgroSmart AI")
st.subheader("AI-Powered Crop Recommendation System")

st.write("""
AgroSmart recommends the best crop based on:
- Soil Nutrients
- Temperature
- Humidity
- Rainfall
- Soil pH
""")


st.header("Enter Agricultural Values")

N = st.number_input(
    "Nitrogen (N)",
    min_value=0.0,
    format="%.2f"
)

P = st.number_input(
    "Phosphorus (P)",
    min_value=0.0,
    format="%.2f"
)

K = st.number_input(
    "Potassium (K)",
    min_value=0.0,
    format="%.2f"
)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=0.0,
    format="%.2f"
)

humidity = st.number_input(
    "Humidity (%)",
    min_value=0.0,
    format="%.2f"
)

ph = st.number_input(
    "Soil pH",
    min_value=0.0,
    format="%.2f"
)

rainfall = st.number_input(
    "Rainfall (mm)",
    min_value=0.0,
    format="%.2f"
)


if st.button("Predict Best Crop"):

    if (
        N == 0 and
        P == 0 and
        K == 0 and
        temperature == 0 and
        humidity == 0 and
        ph == 0 and
        rainfall == 0
    ):

        st.error("Please enter valid values.")

    else:

        input_data = np.array([
            [N, P, K, temperature, humidity, ph, rainfall]
        ])

        prediction = model.predict(input_data)

        st.success(
            f"Recommended Crop: {prediction[0].upper()}"
        )


st.write("---")
st.write(" Empowering Farmers with AI")
