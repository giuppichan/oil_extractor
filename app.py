import streamlit as st
from paddleocr import PaddleOCR

uploaded = st.file_uploader(
    "Upload image",
    type=["png", "jpg", "jpeg"]
)

if uploaded:
    st.image(uploaded)


    ocr = PaddleOCR(
        use_angle_cls=True,
        lang="en"
    )

    result = ocr.ocr(
        uploaded.read()
    )

    st.write(result)
