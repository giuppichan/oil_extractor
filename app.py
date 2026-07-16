import streamlit as st
from rapidocr_onnxruntime import RapidOCR

st.title("OCR Test")

uploaded = st.file_uploader(
    "Upload image",
    type=["png", "jpg", "jpeg"]
)

if uploaded:

    with open("temp.png", "wb") as f:
        f.write(uploaded.getvalue())

    engine = RapidOCR()

    result, _ = engine("temp.png")

    st.write(result)
