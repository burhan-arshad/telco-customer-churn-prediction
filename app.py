import streamlit as st
import pandas as pd
import joblib

model=joblib.load('churn_model.pkl')
scaler=joblib.load('churn_scaler.pkl')
numeric_cols=joblib.load('churn_numeric_cols.pkl')
expected_cols=joblib.load('churn_columns.pkl')

st.title('Customer Churn Predictor')
st.markdown('Fill the following data to get Prediction')

gender = st.selectbox('Gender', ['Female', 'Male']) 
partner = st.selectbox('Has Partner', ['No', 'Yes']) 
dependents = st.selectbox('Has Dependents', ['No', 'Yes']) 
tenure = st.slider('Tenure (months)', 0, 72, 12) 
phone_service = st.selectbox('Phone Service', ['No', 'Yes']) 
paperless = st.selectbox('Paperless Billing', ['No', 'Yes']) 
monthly_charges = st.number_input('Monthly Charges ($)', 0.0, 200.0, 70.0) 

internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No']) 
contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year']) 
payment_method = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']) 

if st.button('Predict Risk'):
    raw={
        'gender': 1 if gender=='Male' else 0,
        'Partner':1 if partner=='Yes' else 0,
        'Dependents': 1 if dependents=='Yes' else 0,
        'tenure': tenure,
        'PhoneService': 1 if phone_service=='Yes' else 0,
        'PaperlessBilling': 1 if paperless =='Yes'else 0,
        'MonthlyCharges': monthly_charges,
        'InternetService_'+internet_service:1,
        'Contract_'+contract:1,
        'PaymentMethod_'+payment_method:1

    }
    input_df=pd.DataFrame([raw])
    for col in expected_cols:
        if col not in input_df.columns:
            input_df[col]=0
    input_df=input_df[expected_cols]
    input_df[numeric_cols] = scaler.transform(input_df[numeric_cols]) 
    prediction = model.predict(input_df)[0] 
    probability = model.predict_proba(input_df)[0][1] 
    if prediction == 1: 
        st.error(f'⚠️ High Churn Risk — {probability:.1%} probability') 
    else: 
        st.success(f'✅ Low Churn Risk — {probability:.1%} probability') 
