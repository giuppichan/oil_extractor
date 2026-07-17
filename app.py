import streamlit as st
import requests

uploaded = st.file_uploader(
    "Upload image",
    type=["png", "jpg", "jpeg"]
)

if uploaded:

    st.image(uploaded)

    response = requests.post(
        "https://api.ocr.space/parse/image",
        files={"filename": open(uploaded, "rb")},
        data={
            "apikey": "your_key",
            "language": "eng"
        }
    )
