import streamlit as st
import pickle
import pandas as pd

# ======================
# Load Model
# ======================
with open("california_house_model.pkl", "rb") as f:
    model = pickle.load(f)

# Extract ocean categories from encoder
ocean_categories = model.named_steps["preprocessor"]\
    .transformers_[1][1]\
    .named_steps["encoder"]\
    .categories_[0]

ocean_list = list(ocean_categories)

# ======================
# Page Config
# ======================
st.set_page_config(page_title="California House Price Predictor", layout="centered")

st.title("🏡 California House Price Prediction")
st.write("Enter housing details to estimate price")

# ======================
# Inputs
# ======================

longitude = st.number_input("Longitude", value=-118.0)

latitude = st.number_input("Latitude", value=34.0)

housing_median_age = st.number_input("Housing Median Age", min_value=1, value=20)

total_rooms = st.number_input("Total Rooms", min_value=1, value=1000)

total_bedrooms = st.number_input("Total Bedrooms", min_value=1, value=200)

population = st.number_input("Population", min_value=1, value=500)

households = st.number_input("Households", min_value=1, value=200)

median_income = st.number_input("Median Income", min_value=0.1, value=3.0)

ocean_proximity = st.selectbox(
    "Ocean Proximity",
    options=ocean_list,
    index=None,
    placeholder="Select ocean proximity"
)

rooms_per_household = st.number_input("Rooms per Household", value=3.0)

bedrooms_ratio = st.number_input("Bedrooms Ratio", value=0.2)

population_per_household = st.number_input("Population per Household", value=2.5)

# ======================
# Prediction
# ======================

if st.button("Predict Price"):

    if ocean_proximity is None:
        st.warning("Please select ocean proximity")

    else:

        input_data = {
            "longitude": longitude,
            "latitude": latitude,
            "housing_median_age": housing_median_age,
            "total_rooms": total_rooms,
            "total_bedrooms": total_bedrooms,
            "population": population,
            "households": households,
            "median_income": median_income,
            "ocean_proximity": ocean_proximity,
            "rooms_per_household": rooms_per_household,
            "bedrooms_ratio": bedrooms_ratio,
            "population_per_household": population_per_household
        }

        input_df = pd.DataFrame(input_data, index=[0])

        prediction = model.predict(input_df)[0]

        st.success(f"Estimated House Price: ${prediction:,.2f}")