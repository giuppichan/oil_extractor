import streamlit as st
from PIL import Image
import pytesseract

uploaded = st.file_uploader(
    "Upload image",
    type=["png", "jpg", "jpeg"]
)

if uploaded:
    img = Image.open(uploaded)

    st.image(img)

    try:
        text = pytesseract.image_to_string(img)

        st.text_area(
            "OCR output",
            text,
            height=300,
        )

    except Exception as e:
        st.error(str(e))
