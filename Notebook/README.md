# 🛒 E-Commerce Order Return Prediction

An end-to-end Machine Learning project that predicts whether an online order is likely to be **Returned** or **Not Returned** using customer, product, and order information.

The application provides probability-based predictions and business recommendations through an interactive Streamlit dashboard.

🔗 **Live Demo:** https://ecommerce-order-return-prediction.streamlit.app/

---

## 📌 Problem Statement

Product returns are a major challenge in e-commerce, increasing operational costs and affecting customer satisfaction.

This project aims to predict whether an order is likely to be returned before shipping so businesses can make better decisions and reduce unnecessary return costs.

---

## 🚀 Features

- Predict whether an order will be Returned or Not Returned
- Return probability estimation
- Business-friendly recommendation system
- Interactive Streamlit dashboard
- Order summary before prediction
- Customer, Product, and Order information input
- Clean and responsive UI
- Probability visualization using Plotly

---

## 🛠 Tech Stack

### Programming Language

- Python

### Machine Learning

- CatBoost Classifier
- Scikit-learn
- Joblib

### Data Processing

- Pandas
- NumPy

### Visualization

- Plotly

### Web Framework

- Streamlit

---

## 📂 Project Structure

```
Ecommerce-Order-Return-Prediction/
│
├── Model/
│   ├── ecommerce_order_return_prediction_model_v1.pkl
│   └── options.pkl
│
├── Notebook/
│   ├── Project.ipynb
│   └── README.md
│
├── .streamlit/
│   └── config.toml
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📊 Input Features

### Customer Information

- Customer Age
- User Title
- Customer Total Orders
- Customer Return Rate
- User State

### Product Information

- Item Price
- Brand ID
- Item Color
- Size Type
- Size Value
- Waist Size
- Inseam Size

### Order Information

- Order Month
- Order Day

---

## 📈 Prediction Output

The application displays:

- Prediction (Returned / Not Returned)
- Return Probability
- Risk Level
- Probability Distribution
- Business Recommendation

---

## 💡 Business Recommendation

Depending on the predicted probability, the application recommends actions such as:

- Ready to Process
- Review Recommended
- Review Before Shipping
- High Return Risk

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Paras0205/Ecommerce-Order-Return-Prediction.git
```

Move into the project directory

```bash
cd Ecommerce-Order-Return-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📦 Libraries Used

- streamlit
- pandas
- numpy
- scikit-learn
- catboost
- plotly
- joblib

---

## 🎯 Future Improvements

- Explainable AI using SHAP values
- Customer return history visualization
- Batch prediction using CSV upload
- Model comparison dashboard
- Deployment with Docker
- API integration

---

## 👨‍💻 Author

**Paras**

Data Analyst | Machine Learning Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
