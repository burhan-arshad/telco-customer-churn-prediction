# Telco Customer Churn Predictor

A Machine Learning application that predicts whether a telecom customer is likely to churn based on their demographics, services, account information, and billing details.

## 🚀 Live Demo

https://telco-customer-churn-prediction-burhan.streamlit.app/

## 📌 Project Overview

Customer churn is an important problem for telecom companies. This project uses Machine Learning to predict whether a customer is likely to leave the company.

The project covers the basic Machine Learning workflow:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Feature selection
* Categorical feature encoding
* Train-test split
* Classification model training
* Model evaluation
* Streamlit deployment

## 📊 Dataset

The project uses the **Telco Customer Churn** dataset from Kaggle.

**Dataset:**
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

The target variable is:

* `Yes` → Customer churned
* `No` → Customer stayed

## 🔍 Features

The model uses customer information such as:

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure
* Internet Service
* Online Security
* Tech Support
* Contract
* Payment Method
* Monthly Charges
* Total Charges

## 🤖 Machine Learning

This is a binary classification problem where the model predicts:

```text
0 → Customer stays
1 → Customer churns
```

Model performance is evaluated using metrics such as:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

## 🖥️ Streamlit App

The trained model is integrated into a Streamlit web application.

Users can enter customer details and get a churn prediction directly through the web interface.

## 🛠️ Tech Stack

* Python
* pandas
* NumPy
* scikit-learn
* Matplotlib
* Seaborn
* Streamlit

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/burhan-arshad/telco-customer-churn-prediction.git
cd telco-customer-churn-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 👨‍💻 Author

**Burhan Arshad**

GitHub: https://github.com/burhan-arshad
