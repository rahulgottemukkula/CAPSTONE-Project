import streamlit as st
import pandas as pd
import pickle
import os


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)


# ---------------------------------------------------
# Load Model
# ---------------------------------------------------

model_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "best_model.pkl"
)

try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)

except Exception as e:
    st.error("❌ Unable to load the machine learning model.")
    st.write("Model path:")
    st.code(model_path)

    st.exception(e)

    st.stop()


# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("❤️ Heart Disease Prediction System")

st.write(
    "Enter the patient's medical information below "
    "to predict the possibility of heart disease."
)

st.divider()


# ---------------------------------------------------
# Input Fields
# ---------------------------------------------------

col1, col2 = st.columns(2)


# ---------------------------------------------------
# Column 1
# ---------------------------------------------------

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=50
    )

    sex = st.selectbox(
        "Sex",
        ["Female", "Male"]
    )

    cp = st.selectbox(
        "Chest Pain Type",
        [0, 1, 2, 3]
    )

    trestbps = st.number_input(
        "Resting Blood Pressure",
        min_value=50,
        max_value=250,
        value=120
    )

    chol = st.number_input(
        "Cholesterol",
        min_value=50,
        max_value=700,
        value=200
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dl",
        [0, 1]
    )

    restecg = st.selectbox(
        "Resting ECG",
        [0, 1, 2]
    )


# ---------------------------------------------------
# Column 2
# ---------------------------------------------------

with col2:

    thalach = st.number_input(
        "Maximum Heart Rate",
        min_value=50,
        max_value=250,
        value=150
    )

    exang = st.selectbox(
        "Exercise Induced Angina",
        [0, 1]
    )

    oldpeak = st.number_input(
        "Oldpeak",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1
    )

    slope = st.selectbox(
        "Slope",
        [0, 1, 2]
    )

    ca = st.selectbox(
        "Number of Major Vessels",
        [0, 1, 2, 3]
    )

    thal = st.selectbox(
        "Thal",
        [3, 6, 7]
    )


# ---------------------------------------------------
# Convert Sex
# ---------------------------------------------------

sex_value = 0 if sex == "Female" else 1


# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

st.divider()

if st.button(
    "🔍 Predict Heart Disease",
    type="primary",
    use_container_width=True
):

    # Create DataFrame
    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex_value],
        "cp": [cp],
        "trestbps": [trestbps],
        "chol": [chol],
        "fbs": [fbs],
        "restecg": [restecg],
        "thalach": [thalach],
        "exang": [exang],
        "oldpeak": [oldpeak],
        "slope": [slope],
        "ca": [ca],
        "thal": [thal]
    })


    # ------------------------------------------------
    # Make Prediction
    # ------------------------------------------------

    try:

        prediction = model.predict(input_data)[0]

    except Exception as e:

        st.error("❌ Prediction failed.")

        st.write("Input sent to model:")

        st.dataframe(input_data)

        st.exception(e)

        st.stop()


    # ------------------------------------------------
    # Display Result
    # ------------------------------------------------

    st.subheader("🔎 Prediction Result")


    if prediction == 1:

        st.error(
            "⚠️ Higher possibility of Heart Disease"
        )

    else:

        st.success(
            "✅ Lower possibility of Heart Disease"
        )


    # ------------------------------------------------
    # Patient Information
    # ------------------------------------------------

    st.subheader("👤 Patient Details")

    st.dataframe(
        input_data,
        use_container_width=True
    )