from flask import session
from PIL import Image
import google.generativeai as genai

# Helper function to process images
def process_images(uploaded_files):
    image_parts_list = []
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            bytes_data = uploaded_file.read()
            image_part = {
                "mime_type": uploaded_file.mimetype,
                "data": bytes_data
            }
            image_parts_list.append(image_part)
    return image_parts_list

# Helper function to get Gemini response
def get_gemini_response(input_text, image_parts, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, *image_parts, prompt])
    return response.text