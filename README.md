# **Life Expectancy Prediction Project**

## **Project Overview**
This project predicts life expectancy based on socio-economic and health indicators using machine learning models. It provides insights into the factors influencing life expectancy and demonstrates how predictive analytics can be applied to public health and policy-making.

---

## **Features**
- **User Input:**
  - Users can input socio-economic and health indicators like adult mortality, alcohol consumption, GDP, schooling, and immunization rates.
- **Model Selection:**
  - Choose from pre-trained models, including Linear Regression, Random Forest, Gradient Boosting, Support Vector Regression, and MLP.
- **Predictions:**
  - Displays the predicted life expectancy based on user inputs.
- **Visualization:**
  - Supports visualization of input data to ensure meaningful and accurate predictions.

---

## **Project Structure**
```plaintext
.
├── app.py                  # Main Streamlit app script
├── models/
│   ├── linear_regression_model.pkl
│   ├── random_forest_model.pkl
│   ├── svr_model.pkl
│   ├── mlp_model.pkl
│   └── ...
├── encoders/
│   ├── label_encoder_status.pkl
│   ├── scaler.pkl
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── data/
│   └── life_expectancy.csv # Dataset for model training and testing
```

---

## **How to Run the Project**

### **1. Prerequisites**
Ensure Python 3.8 or later is installed. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### **2. Directory Setup**
- Place the pre-trained models in the `models/` directory:
  - `linear_regression_model.pkl`
  - `random_forest_model.pkl`
  - `svr_model.pkl`
  - `mlp_model.pkl`
- Place required encoders (e.g., label encoders, scalers) in the `encoders/` directory.

### **3. Run the Application**
Start the Streamlit app:

```bash
streamlit run app.py
```

---

## **Using the Application**

1. **Select a Model:**
   - Use the sidebar to select a predictive model (e.g., Linear Regression, Random Forest, SVR, or MLP).

2. **Input Data:**
   - Enter values for socio-economic and health indicators, such as:
     - **Status:** Developed or Developing.
     - **Adult Mortality (per 1000):** Mortality rate in adults.
     - **GDP (per capita):** Gross Domestic Product per capita.
     - **Schooling (years):** Average years of schooling.
     - **Immunization Rates:** Immunization percentages for diseases like polio and diphtheria.

3. **Predict:**
   - Click the **Predict Life Expectancy** button to get the predicted life expectancy.

4. **View Results:**
   - The app displays the predicted life expectancy and provides options to adjust inputs for further exploration.

---

## **Dependencies**
The project requires the following Python libraries:
- `streamlit`
- `pandas`
- `numpy`
- `scikit-learn`
- `pickle`
- `matplotlib`

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## **Future Improvements**
- Include data visualization to highlight feature importance and trends.
- Enable batch predictions for datasets instead of single input predictions.
- Integrate advanced models like XGBoost or LightGBM for better accuracy.

---

## **Acknowledgments**
- The dataset used in this project is sourced from publicly available datasets, such as the [WHO Life Expectancy dataset](https://www.kaggle.com/kumarajarshi/life-expectancy-who).
- Thanks to the open-source community for tools like Streamlit and Scikit-learn.
