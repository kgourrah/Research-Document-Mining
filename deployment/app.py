
import streamlit as st
import joblib

# Load trained model
model = joblib.load("best_model.joblib")

# Web interface
st.title("Research Paper Classification")
st.write("Enter a research abstract to classify the research paper.")

abstract = st.text_area("Research Abstract")

if st.button("Classify Research Paper"):

    if abstract.strip():

        prediction = model.predict([abstract])[0]

        st.subheader("Classification Result")
        st.success("Predicted Category: " + prediction.upper())

    else:
        st.warning("Please enter a research abstract.")
