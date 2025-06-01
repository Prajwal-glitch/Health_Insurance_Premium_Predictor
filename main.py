import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Health Insurance Premium Predictor", layout="wide")

# --- Title ---
st.markdown(
    "<h2 style='text-align: center; color: #4CAF50;'>🏥 Health Insurance Premium Predictor</h2><hr>",
    unsafe_allow_html=True
)

# --- Categorical Options ---
options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold'],
    'Physical Activity': ['Low', 'Medium', 'High'],
    'Stress Level': ['Low', 'Medium', 'High'],
    'Income Level': ['<10L', '10L - 25L', '25L - 40L', '> 40L']
}

# --- Section: Personal Details ---
st.markdown("### 👤 Personal Details")
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('Age', min_value=18, max_value=100, step=1)
    gender = st.selectbox('Gender', options['Gender'])
    income_level = st.selectbox('Income Level', options['Income Level'])

with col2:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, max_value=20, step=1)
    marital_status = st.selectbox('Marital Status', options['Marital Status'])
with col3:
    region = st.selectbox('Region', options['Region'])
    employment_status = st.selectbox('Employment Status', options['Employment Status'])


# --- Section: Health Details ---
st.markdown("### 🩺 Health Details")
col4, col5, col6 = st.columns(3)
with col4:
    bmi_category = st.selectbox('BMI Category', options['BMI Category'])
    stress_level = st.selectbox('Stress Level', options['Stress Level'])

with col5:
    smoking_status = st.selectbox('Smoking Status', options['Smoking Status'])
    medical_history = st.selectbox('Medical History', options['Medical History'])

with col6:
    physical_activity = st.selectbox('Physical Activity', options['Physical Activity'])

# --- Section: Insurance Info ---
st.markdown("### 💼 Insurance Information")
col7, col8, col9 = st.columns(3)
with col7:
    insurance_plan = st.selectbox('Insurance Plan', options['Insurance Plan'])

# --- Prepare Input Dictionary ---
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history,
    'Physical Activity': physical_activity,
    'Stress Level': stress_level,
    'Income Level': income_level
}

# --- Prediction Button ---
st.markdown("<hr>", unsafe_allow_html=True)
if st.button('🔍 Predict Insurance Premium'):
    prediction = predict(input_dict)
    st.success(f"💰 **Estimated Annual Premium:** ₹ {prediction:,}")

