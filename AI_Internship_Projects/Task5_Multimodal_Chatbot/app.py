import streamlit as st
from PIL import Image
from transformers import pipeline

# Load model
captioner = pipeline(
    "image-text-to-text",
    model="Salesforce/blip-image-captioning-base"
)

# Streamlit UI
st.title("Multi-Modal AI Chatbot 🤖🖼️")

st.write("Upload an image or ask questions.")

# Text chatbot
user_text = st.text_input("Enter your message:")

if user_text:

    st.subheader("Chatbot Response")

    st.success(f"You said: {user_text}")

# Upload image
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.subheader("Image Understanding")

    # Generate caption
    result = captioner(
        images=image,
        text="Describe this image"
    )

    caption = result[0]["generated_text"]

    st.success(caption)