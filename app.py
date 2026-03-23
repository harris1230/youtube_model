import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("📺 YouTube Views Predictor")

st.write("Enter video details:")

likes = st.number_input("Likes", min_value=0)
comments = st.number_input("Comments", min_value=0)
title_length = st.number_input("Title Length", min_value=1)

if st.button("Predict"):
    result = model.predict([[likes, comments, title_length]])
    st.success(f"Estimated Views: {int(result[0])}")