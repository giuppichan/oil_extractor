import streamlit as st
from doctr.io import DocumentFile

st.title("OCR Test")

uploaded = st.file_uploader(
    "Upload image",
    type=["png", "jpg", "jpeg"]
)

if uploaded:

    st.image(uploaded)
