
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("ckd_model.pkl", "rb"))

st.title("CKD Prediction App")

age = st.number_input("Age", min_value=1)
bp = st.number_input("Blood Pressure")
sg = st.number_input("Specific Gravity")
al = st.number_input("Albumin")
su = st.number_input("Sugar")
hemo = st.number_input("Hemoglobin")

if st.button("Predict"):
    data = np.array([[age, bp, sg, al, su, hemo]])
    result = model.predict(data)
    if result[0] == 0:
        st.error("You may have Chronic Kidney Disease.")
    else:
        st.success("No signs of CKD.")
