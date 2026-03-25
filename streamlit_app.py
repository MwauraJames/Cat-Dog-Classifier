import streamlit as st
import requests
from PIL import Image

API_URL = "https://jamezmw-cat-dog-api.hf.space/predict"

st.title("🐱 Cat vs Dog Classifier 🐶")
st.write("Upload an image and the model will tell you if it's a cat or a dog!")

uploaded_file=st.file_uploader("Choose an image", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

    with st.spinner("Classifying..."):
        uploaded_file.seek(0)
        files = {"file": (uploaded_file.name, uploaded_file, "image/jpeg")}
        response = requests.post(API_URL, files=files, timeout=30)
        st.write(f"Status code: {response.status_code}")
        st.write(f"Response: {response.text}")
        result = response.json()

    prediction=result["prediction"]
    confidence=result["confidence"]*100

    if prediction == "dog":
        st.success(f"🐶 It's a **Dog!** ({confidence:.1f}% confidence)")
    else:
        st.success(f"🐱 It's a **Cat!** ({confidence:.1f}% confidence)")
