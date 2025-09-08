import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import pickle 

# =========================
# Load Model + Transformers
# =========================
model = tf.keras.models.load_model("model.h5")

with open("label_encoder_gender.pkl", "rb") as file:
    label_encoder_gender = pickle.load(file)

with open("onehot_encoder_geo.pkl", "rb") as file:
    onehot_encoder_geo = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

# =========================
# Streamlit UI
# =========================
st.title("📊 Customer Churn Prediction")

geography = st.selectbox("Geography", onehot_encoder_geo.categories_[0])
gender = st.selectbox("Gender", label_encoder_gender.classes_)
age = st.slider("Age", 18, 92)
balance = st.number_input("Balance", min_value=0.0, step=100.0)
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, step=1)
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, step=100.0)
tenure = st.slider("Tenure (Years)", 0, 10)
num_of_products = st.slider("Number of Products", 1, 4)
has_cr_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])

# =========================
# Prepare Input Data
# =========================
# Numeric + label encoded
input_data = pd.DataFrame({
    "CreditScore": [credit_score],
    "Gender": [label_encoder_gender.transform([gender])[0]],
    "Age": [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [num_of_products],
    "HasCrCard": [has_cr_card],
    "IsActiveMember": [is_active_member],
    "EstimatedSalary": [estimated_salary]
})

# One-hot encode Geography safely (convert sparse → dense array)
geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()

geo_encoded_df = pd.DataFrame(
    geo_encoded,
    columns=onehot_encoder_geo.get_feature_names_out()
)

# Merge numeric + encoded categorical
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

# =========================
# Scale Features
# =========================
input_data_scaled = scaler.transform(input_data)

# =========================
# Prediction
# =========================
if st.button("🔮 Predict"):
    prediction = model.predict(input_data_scaled)
    prediction_proba = prediction[0][0]

    if prediction_proba > 0.5:
        st.error(f"⚠️ The customer is likely to CHURN (probability = {prediction_proba:.2f})")
    else:
        st.success(f"✅ The customer is NOT likely to churn (probability = {prediction_proba:.2f})")
