import streamlit as st
import pickle
import pandas as pd

# ======================
# Load Model
# ======================
with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Extract locations from pipeline
locations = model.named_steps['columntransformer']\
    .transformers_[0][1].categories_[0]

location_list = list(locations)

# ======================
# Page Config
# ======================
st.set_page_config(page_title="Bangalore House Price Prediction", layout="centered")

st.title("🏠 Bangalore House Price Prediction")
st.write("Enter house details to estimate price")

# ======================
# Inputs
# ======================

location = st.selectbox(
    "Search or type a location",
    options=location_list,
    index=None,
    placeholder="Start typing location...",
    accept_new_options=True
)

total_sqft = st.number_input("Total Square Feet", min_value=100, value=1000)

bath = st.number_input("Number of Bathrooms", min_value=1, value=2)

bhk = st.number_input("Number of BHK", min_value=1, value=2)

# ======================
# Prediction
# ======================

if st.button("Predict Price"):

    if location is None:
        st.warning("Please enter a location")

    else:

        # Case-insensitive location check
        search = location.strip().lower()
        dataset_locations = [loc.lower() for loc in location_list]

        if search not in dataset_locations:
            st.error("❌ Location not recognized")

        else:
            correct_location = location_list[dataset_locations.index(search)]

            input_df = pd.DataFrame(
                [[correct_location, total_sqft, bath, bhk]],
                columns=["location","total_sqft","bath","bhk"]
            )

            prediction = model.predict(input_df)[0]

            price_rupees = round(prediction * 100000)

            st.success(f"Estimated House Price: ₹ {price_rupees:,}")