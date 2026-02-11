import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("loan_approval_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Loan Approval Prediction", layout="centered")

st.title("🏦 Loan Approval Prediction App")
st.write("Enter applicant details to predict loan approval status")

# ======================
# User Inputs
# ======================
no_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=1)

graduation = st.selectbox("Graduated", ["Yes", "No"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

income_annum = st.number_input("Annual Income", min_value=0, value=300000)
loan_amount = st.number_input("Loan Amount", min_value=0, value=1000000)
loan_term = st.number_input("Loan Term (Years)", min_value=1, max_value=30, value=10)
cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, value=700)

residential_assets_value = st.number_input("Residential Assets Value", min_value=0, value=1000000)
commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0, value=0)
luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0, value=0)
bank_asset_value = st.number_input("Bank Asset Value", min_value=0, value=50000)

# Convert categorical values
graduation = 1 if graduation == "Yes" else 0
self_employed = 1 if self_employed == "Yes" else 0

# ======================
# Prediction
# ======================
if st.button("Predict Loan Status"):
    input_data = pd.DataFrame([{
        "no_of_dependents": no_of_dependents,
        "education": graduation,
        "self_employed": self_employed,
        "income_annum": income_annum,
        "loan_amount": loan_amount,
        "loan_term": loan_term,
        "cibil_score": cibil_score,
        "residential_assets_value": residential_assets_value,
        "commercial_assets_value": commercial_assets_value,
        "luxury_assets_value": luxury_assets_value,
        "bank_asset_value": bank_asset_value
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")