import streamlit as st
import requests

st.title("✈️ AI Travel Booking Assistant")

query = st.text_input("Describe your travel plan")

if st.button("Book"):
    r = requests.post(
        "http://localhost:8000/chat",
        json={"message": query}
    )
    st.json(r.json())
