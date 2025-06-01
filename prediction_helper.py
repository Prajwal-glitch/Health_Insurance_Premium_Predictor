# prediction_helper.py

import pandas as pd
import joblib

# Load model
model = joblib.load("artifacts/model.joblib")

# Risk score mapping
def calculate_total_risk(medical_history):
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }
    diseases = medical_history.lower().split(" & ")
    return sum(risk_scores.get(d, 0) for d in diseases)

# Preprocess user input for model
def preprocess_input(input_dict):
    expected_columns = [
        'age', 'physical_activity', 'stress_level', 'number_of_dependants',
        'income_level', 'insurance_plan', 'total_risk_score', 'gender_Male',
        'region_Northwest', 'region_Southeast', 'region_Southwest',
        'marital_status_Unmarried', 'bmi_category_Obesity',
        'bmi_category_Overweight', 'bmi_category_Underweight',
        'smoking_status_Occasional', 'smoking_status_Regular',
        'employment_status_Salaried', 'employment_status_Self-Employed'
    ]

    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    # Ordinal encodings
    physical_activity_encoding = {'Low': 0, 'Medium': 1, 'High': 2}
    stress_level_encoding = {'Low': 2, 'Medium': 1, 'High': 0}
    income_level_encoding = {'<10L': 0, '10L - 25L': 1, '25L - 40L': 2, '> 40L': 3}
    insurance_plan_encoding = {'Gold': 2, 'Silver': 1, 'Bronze': 0}

    # Assign values
    df['age'] = input_dict['Age']
    df['number_of_dependants'] = input_dict['Number of Dependants']
    df['physical_activity'] = physical_activity_encoding.get(input_dict['Physical Activity'], 1)
    df['stress_level'] = stress_level_encoding.get(input_dict['Stress Level'], 1)
    df['income_level'] = income_level_encoding.get(input_dict['Income Level'], 1)
    df['insurance_plan'] = insurance_plan_encoding.get(input_dict['Insurance Plan'], 1)
    df['total_risk_score'] = calculate_total_risk(input_dict['Medical History'])

    # One-hot encodings
    if input_dict['Gender'] == 'Male':
        df['gender_Male'] = 1
    if input_dict['Region'] == 'Northwest':
        df['region_Northwest'] = 1
    elif input_dict['Region'] == 'Southeast':
        df['region_Southeast'] = 1
    elif input_dict['Region'] == 'Southwest':
        df['region_Southwest'] = 1
    if input_dict['Marital Status'] == 'Unmarried':
        df['marital_status_Unmarried'] = 1
    if input_dict['BMI Category'] == 'Obesity':
        df['bmi_category_Obesity'] = 1
    elif input_dict['BMI Category'] == 'Overweight':
        df['bmi_category_Overweight'] = 1
    elif input_dict['BMI Category'] == 'Underweight':
        df['bmi_category_Underweight'] = 1
    if input_dict['Smoking Status'] == 'Occasional':
        df['smoking_status_Occasional'] = 1
    elif input_dict['Smoking Status'] == 'Regular':
        df['smoking_status_Regular'] = 1
    if input_dict['Employment Status'] == 'Salaried':
        df['employment_status_Salaried'] = 1
    elif input_dict['Employment Status'] == 'Self-Employed':
        df['employment_status_Self-Employed'] = 1

    return df

# Prediction function
def predict(input_dict):
    input_df = preprocess_input(input_dict)
    prediction = model.predict(input_df)
    return int(prediction[0])

