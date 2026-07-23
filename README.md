# 📊 Sales Analytics & Forecasting Dashboard using Machine Learning

An end-to-end Data Analytics project that transforms raw sales data into actionable business insights through interactive dashboards and machine learning-based sales forecasting.

The project enables organizations to monitor key business metrics, analyze sales performance across different dimensions, and forecast future sales for better decision-making.
---
## 🚀 Features

- 📈 Interactive Sales Dashboard
- 📊 KPI Monitoring
- 🔍 Exploratory Data Analysis (EDA)
- 📅 Time-Series Sales Analysis
- 🌍 Regional & Product-wise Sales Analysis
- 👥 Customer Segment Analysis
- 📦 Inventory Planning Insights
- 🤖 Machine Learning Sales Forecasting
- 📉 Model Performance Comparison
- 📥 CSV Dataset Upload Support (Future)
- 🌐 Responsive Web Interface

---

## 🧠 Machine Learning Models

The project compares multiple regression algorithms:

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

Evaluation Metrics:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## 🛠 Tech Stack

### Frontend
- React.js
- Tailwind CSS
- Recharts

### Backend
- FastAPI
- REST API

### Database
- PostgreSQL / Supabase

### Data Analytics
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-learn
- XGBoost

### Tools
- Jupyter Notebook
- VS Code
- Git & GitHub
- Postman
- PostgreSQL
- pgAdmin
- Excel
- Kaggle

---

## 📂 Project Structure

```text
Sales_Analytics_Dashboard/
│
├── backend/
│   ├── api/
│   ├── models/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── assets/
│
├── notebooks/
│   ├── EDA.ipynb
│   └── Model_Training.ipynb
│
├── dataset/
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dashboard Modules

- Executive Dashboard
- Sales Overview
- Revenue Analysis
- Profit Analysis
- Customer Analytics
- Product Performance
- Regional Performance
- Sales Forecasting

---

## 📈 Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis
4. Feature Engineering
5. Dashboard Development
6. Machine Learning Model Training
7. Model Evaluation
8. Deployment

---

## 📁 Dataset

**Source:** Kaggle Superstore Sales Dataset

Dataset contains approximately 10,000 records including:

- Order Date
- Sales
- Profit
- Quantity
- Discount
- Product Category
- Customer Segment
- Region
- State
- Shipping Mode

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/catalyst2004/Sales_Analytics_Dashboard.git
```

Move into the project directory

```bash
cd Sales_Analytics_Dashboard
```

Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Backend

```bash
uvicorn main:app --reload
```

Run Frontend

```bash
npm install
npm run dev
```

---

## 🎯 Future Enhancements

- Authentication System
- Role-Based Access Control
- Real-Time Dashboard
- Live Database Integration
- Inventory Forecasting
- Demand Forecasting
- Customer Churn Prediction
- Cloud Deployment
- Docker Support
- CI/CD Pipeline

---

## 👨‍💻 Author

**Vicky Raj**

B.Tech Computer Science & Engineering

Data Analytics Intern

GitHub: https://github.com/catalyst2004

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
