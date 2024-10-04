from dotenv import load_dotenv

load_dotenv()  # load all the environment variables from .env file

import streamlit as st 
import os
from PIL import Image
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the Gemini Pro vision 
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text, image, prompt):
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file in bytes
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # get the mime type of the uploaded File
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")

# Initialize the Streamlit App
st.set_page_config(page_title="MultiLanguage Invoice", page_icon="📄")
st.header("Gemini Multi language Invoice Extractor")

# Get user input and uploaded file
user_input = st.text_input("Input:", key="input")
uploaded_file = st.file_uploader("Upload the Invoice Here..", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=True)

submit = st.button("Tell me about the Invoice")

# Define the input prompt
input_prompt = '''
You are an expert in understanding invoices. We will upload an 
image as an invoice and you will answer any questions based on the 
uploaded invoice image.
'''

# When Submit is clicked
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(user_input, image_data, input_prompt)

    st.subheader("The Response is")
    st.write(response)
