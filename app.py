import streamlit as st
import random

models = ["autorec", "deepfm", "ncf"]

st.title("Movie Recommendation System")

target_model = st.selectbox("Select Model", models)

user_id = st.text_input("Enter User ID")

if st.button("Get Recommendations"):
    st.write(f"Recommendations for User {user_id} using {target_model} model:")
    st.table({
        "Movie ID": [random.randint(1, 1000) for _ in range(10)],
        "Score": [round(random.uniform(0.7, 1.0), 3) for _ in range(10)]
    })