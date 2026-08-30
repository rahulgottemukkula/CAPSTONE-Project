# ❤️ Heart Disease Prediction Using Machine Learning

## 📌 Project Overview

This project focuses on building a Machine Learning model to predict the possibility of heart disease based on various medical attributes.

The project covers the complete Machine Learning workflow, starting from data collection and exploratory data analysis (EDA), followed by data preprocessing, model training, model evaluation, selection of the best-performing model, and finally deployment using Streamlit.

The trained model is integrated into a user-friendly web application where users can enter patient information and receive a heart disease prediction.

---

## 🎯 Project Objective

The main objective of this project is to develop a Machine Learning classification model that can predict whether a patient has a higher or lower possibility of heart disease based on medical and clinical features.

The project also demonstrates how a Machine Learning model can be converted into a practical application using Streamlit.

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle
- Streamlit
- Jupyter Notebook

---

## 📂 Project Structure

```text
Heart-Disease-Prediction/
│
├── appp.py
├── best_model.pkl
├── heart.csv
├── README.md
│
├── notebooks/
│   └── Heart Disease Prediction Using Machine Learning.ipynb
│
├── documents/
│   └── project_report.pdf
│
└── images/
    ├── streamlit_home.png
    └── prediction_result.png

🔄 Project Workflow

The project follows the complete Machine Learning pipeline:

Data Collection
      ↓
Data Understanding
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Data Preprocessing
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Selection
      ↓
Model Saving
      ↓
Streamlit Deployment
      ↓
Heart Disease Prediction
1️⃣ Data Collection

The dataset contains medical information about patients along with the target variable indicating the presence or absence of heart disease.

The dataset contains the following features:

Feature	Description
age	Age of the patient
sex	Sex of the patient
cp	Chest pain type
trestbps	Resting blood pressure
chol	Serum cholesterol
fbs	Fasting blood sugar
restecg	Resting ECG results
thalach	Maximum heart rate achieved
exang	Exercise-induced angina
oldpeak	ST depression induced by exercise
slope	Slope of the peak exercise ST segment
ca	Number of major vessels
thal	Thalassemia-related feature
target	Target variable
2️⃣ Data Understanding

The dataset was initially explored to understand:

Number of rows and columns
Data types
Missing values
Statistical properties
Unique values
Distribution of the target variable

This step helps in understanding the structure and quality of the dataset before applying Machine Learning algorithms.

3️⃣ Data Cleaning

The dataset was checked for:

Missing values
Duplicate records
Incorrect data types
Invalid or inconsistent values

The required preprocessing steps were performed before training the Machine Learning models.

4️⃣ Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand relationships between different medical features and heart disease.

Various visualizations were used, including:

Histograms
Distribution plots
Count plots
Correlation analysis
Heatmaps
Feature-based visualizations

EDA helped identify important patterns and relationships within the dataset.

📊 Correlation Analysis

A correlation heatmap was used to understand the relationships between numerical features and the target variable.

5️⃣ Data Preprocessing

The data was prepared for Machine Learning by performing the required preprocessing operations.

This included:

Encoding categorical variables
Separating independent and dependent variables
Preparing the feature matrix
Preparing the target variable
Splitting the dataset into training and testing sets

The final model uses the following 13 input features:

age
sex
cp
trestbps
chol
fbs
restecg
thalach
exang
oldpeak
slope
ca
thal
6️⃣ Train-Test Split

The dataset was divided into training and testing datasets.

The training data was used to train the Machine Learning models, while the testing data was used to evaluate their performance on unseen data.

7️⃣ Machine Learning Models

Different classification algorithms were trained and evaluated to determine which model performs best for this dataset.

The models included in the analysis were selected and compared based on their performance metrics.

The main evaluation metrics considered were:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix
8️⃣ Model Evaluation

After training the models, their performance was evaluated using the test dataset.

The models were compared based on their evaluation results, and the best-performing model was selected for deployment.

9️⃣ Best Model

After comparing the trained models, the best-performing model was selected and saved using Python's pickle module.

The saved model is:

best_model.pkl

This file is later loaded by the Streamlit application to make predictions on new patient data.

🔟 Streamlit Web Application

A Streamlit-based frontend was developed to make the Machine Learning model interactive.

The application allows users to enter patient medical information through a simple web interface.

The application accepts the following inputs:

Age
Sex
Chest Pain Type
Resting Blood Pressure
Cholesterol
Fasting Blood Sugar
Resting ECG
Maximum Heart Rate
Exercise-Induced Angina
Oldpeak
Slope
Number of Major Vessels
Thal

The entered information is converted into the required format and passed to the trained Machine Learning model.

🖥️ Streamlit Application

🔮 Prediction Result

After entering the patient information and clicking the prediction button, the application displays the model's prediction.

The application provides one of two outcomes:

Higher possibility of Heart Disease

or

Lower possibility of Heart Disease
▶️ How to Run the Project
Step 1: Clone the Repository
git clone <your-repository-url>
Step 2: Navigate to the Project Folder
cd Heart-Disease-Prediction
Step 3: Install Required Libraries
pip install numpy pandas matplotlib seaborn scikit-learn streamlit
Step 4: Run the Streamlit Application
streamlit run appp.py

The application will open in your browser.

📊 Project Highlights
Complete Machine Learning workflow
Exploratory Data Analysis
Data preprocessing
Multiple classification models
Model evaluation and comparison
Best model selection
Model serialization using Pickle
Interactive Streamlit frontend
Real-time prediction using user inputs
📁 Project Files
Heart Disease Prediction Using Machine Learning.ipynb

Contains the complete Machine Learning workflow including:

Data analysis
EDA
Preprocessing
Model training
Model evaluation
Model selection
best_model.pkl

Contains the trained Machine Learning model used by the Streamlit application.

appp.py

Contains the Streamlit application used to create the prediction interface.

heart.csv

Original dataset used for developing the Machine Learning model.

project_report.pdf

Detailed documentation and report of the project.

⚠️ Disclaimer

This project is developed for educational and demonstration purposes.

The predictions generated by this application should not be considered a medical diagnosis or a substitute for professional medical advice.

👨‍💻 Author

Rahul Gottemukkula

Machine Learning / Data Science Project


### One thing I recommend changing

Don't add all those image sections **until you've actually uploaded the corresponding images**.

For your current project, I'd use these four:

```text
images/
├── streamlit_home.png
├── prediction_result.png
├── correlation_heatmap.png
└── model_comparison.png
