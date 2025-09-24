# 🏥 Health Insurance Premium Predictor  

An interactive ML-powered web app that predicts **health insurance premiums** based on user details such as age, BMI, smoking status, and medical history.  
Built with **Scikit-learn**, **XGBoost**, and **Streamlit**.  

🔗 **Live Demo** – [Streamlit App](https://healthinsurancepremiumpredictor.streamlit.app/)  

---

## 🚀 Features  

- **🧹 Data Cleaning & Preprocessing** – Handled duplicates, missing values, outliers, categorical encoding, and feature scaling.  
- **📊 Exploratory Data Analysis (EDA)** – Visualized feature distributions, correlations, and relationships using seaborn & matplotlib.  
- **⚙️ Regression Models** – Linear Regression, Random Forest, and XGBoost compared for accuracy and error metrics.  
- **🔧 Hyperparameter Tuning** – Applied **RandomizedSearchCV** to optimize model performance.  
- **📈 Model Evaluation** – Achieved **R² score: 0.99** and **RMSE: 680** on test dataset.  
- **🌐 Deployment** – Interactive **Streamlit app** for real-time premium prediction.  

---

## 📖 Machine Learning Lifecycle  

1. **Problem Definition** – Predict health insurance premium from user demographics and medical history.  
2. **Data Collection** – Used a dataset of **10,000 records** in CSV format.  
3. **Data Preprocessing & EDA** – Removed duplicates, treated missing values & outliers, encoded categorical variables, and visualized distributions.  
4. **Feature Engineering** – Created domain-specific features and applied scaling while preventing data leakage.  
5. **Modeling** – Trained Linear Regression, Random Forest, and XGBoost; selected **XGBoost** after tuning.  
6. **Evaluation** – Validated model with **RMSE (680)**, **MSE**, and **R² (0.99)**.  
7. **Deployment** – Streamlit web app for real-time user predictions.  

---

## 🖼️ Screenshot  

![App Screenshot](screenshot.png)  

---

## 🛠️ Tools & Technologies  

- **Languages & Frameworks**: Python, Streamlit  
- **Libraries**: pandas, numpy, seaborn, matplotlib, scikit-learn, xgboost, statsmodels  

---

## 🛠️ Installation  

```bash
# Clone this repository
git clone https://github.com/your-username/health-insurance-premium-predictor.git
cd health-insurance-premium-predictor

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run main.py
