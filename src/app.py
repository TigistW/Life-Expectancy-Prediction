from imports import *
from utils.load_model import load_model
from utils.predict import predict_with_model
from utils.countries_list import countries
import streamlit as st
from PIL import Image
import pandas as pd

# Load all models
@st.cache_data
def load_all_models():
    models = {
        "Linear_Regression": load_model("../models/linear_regression_model.pkl"),
        "Random_Forest_Untuned": load_model("../models/random_forest_model.pkl"),
        "Random_Forest_Tuned": load_model("../models/tuned_random_forest_model.pkl"),
        "Gradient_Boosting_Untuned": load_model("../models/gradient_boosting_model.pkl"),
        "Gradient_Boosting_Tuned": load_model("../models/tuned_gradient_boosting_model.pkl"),
        "SVR_Untuned": load_model("../models/svr_model.pkl"),
        "MLP": load_model("../models/mlp_model.pkl"),
    }
    return models

def load_all_encoder():
    encoders = {
        "Status_Encoder": load_model("../encoders/label_encoder_status.pkl"),
        "Standard_Scalar": load_model("../encoders/scaler.pkl")
    }
    return encoders

# Load models and encoders
models = load_all_models()
encoders = load_all_encoder()

# Sidebar: Add a title and model selection
st.sidebar.title("Model Selection")
model_choice = st.sidebar.radio(
    "Choose a model for prediction:",
    list(models.keys())
)
st.sidebar.write(f"### Model: **{model_choice}**")

# Streamlit app title
st.title("_Life expectancy prediction_")
st.write("""
###### Choose a model and predict life expectancy based on socio-economic and health indicators.
""")

# Input fields for user data
def user_inputs():
    col1, col2 = st.columns(2)  # Divide the layout into two columns

    # First row of inputs
    with col1:
        country = st.selectbox("Select Country", countries)
        year = st.slider("Year", min_value=2000, max_value=2023, value=2020, step=1)
        status = st.selectbox("Status", ["Developed", "Developing"])
        adult_mortality = st.slider("Adult Mortality (per 1000)", min_value=0, max_value=1000, value=200, step=10)
        # infant_deaths = st.slider("Infant Deaths (per 1000)", min_value=0, max_value=1000, value=10, step=1)
        alcohol = st.slider("Alcohol Consumption (liters per capita)", min_value=0.0, max_value=20.0, value=5.0, step=0.5)
        percentage_expenditure = st.slider("Percentage Expenditure on Health", min_value=0.0, max_value=20000.0, value=1000.0, step=10.0)
        hepatitis_b = st.slider("Hepatitis B Immunization (%)", min_value=0.0, max_value=100.0, value=80.0, step=1.0)
        measles = st.slider("Measles Cases", min_value=0, max_value=100000, value=10, step=100)
        # bmi = st.slider("Average BMI", min_value=0.0, max_value=100.0, value=25.0, step=0.1)
        under_five_deaths = st.slider("Under-5 Deaths (per 1000)", min_value=0, max_value=1000, value=15, step=1)
    # Second row of inputs
    with col2:
        polio = st.slider("Polio Immunization (%)", min_value=0.0, max_value=100.0, value=90.0, step=1.0)
        total_expenditure = st.slider("Total Health Expenditure (% of GDP)", min_value=0.0, max_value=100.0, value=6.0, step=0.5)
        diphtheria = st.slider("Diphtheria Immunization (%)", min_value=0.0, max_value=100.0, value=85.0, step=1.0)
        hiv_aids = st.slider("HIV/AIDS Deaths (per 1000)", min_value=0.0, max_value=100.0, value=1.0, step=0.5)
        gdp = st.slider("GDP per Capita", min_value=0.0, max_value=100000.0, value=10000.0, step=100.0)
        population = st.slider("Population (in millions)", min_value=0.0, max_value=2000.0, value=50.0, step=1.0)
        thinness_1_19 = st.slider("Thinness 1-19 Years (%)", min_value=0.0, max_value=100.0, value=10.0, step=1.0)
        # thinness_5_9 = st.slider("Thinness 5-9 Years (%)", min_value=0.0, max_value=100.0, value=10.0, step=1.0)
        income_composition = st.slider("Income Composition of Resources", min_value=0.0, max_value=1.0, value=0.8, step=0.01)
        schooling = st.slider("Schooling (Years)", min_value=0.0, max_value=20.0, value=12.0, step=0.1)
        
    encoded_status = encoders["Status_Encoder"].transform([status])[0]

    features = pd.DataFrame({
        # "Year": [year],
        "Status": [encoded_status],
        "Adult Mortality": [adult_mortality],
        # "infant deaths": [infant_deaths],
        "Alcohol": [alcohol],
        "percentage expenditure": [percentage_expenditure],
        "Hepatitis B": [hepatitis_b],
        "Measles ": [measles],
        # " BMI ": [bmi],
        "under-five deaths ": [under_five_deaths],
        "Polio": [polio],
        "Total expenditure": [total_expenditure],
        "Diphtheria ": [diphtheria],
        " HIV/AIDS": [hiv_aids],
        "GDP": [gdp],
        "Population": [population],
        " thinness  1-19 years": [thinness_1_19],
        # " thinness 5-9 years": [thinness_5_9],
        "Income composition of resources": [income_composition],
        "Schooling": [schooling],
    })
    return features

# Get user inputs
input_data = user_inputs()

# Show user input
st.write("### User Inputs:")
st.write(input_data)

# Predict button
if st.button("Predict Life Expectancy"):
    selected_model = models[model_choice]
    prediction = predict_with_model(selected_model, input_data)
    st.write(f"### Predicted Life Expectancy: **{prediction[0]:.2f} years**")
