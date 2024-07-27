import streamlit as st
from PIL import Image
from rembg import remove
import numpy as np
import io

def remove_background(input_image):
    # Convert the image to a numpy array
    input_image_np = np.array(input_image)
    
    # Use rembg to remove the background
    output_image_np = remove(input_image_np)
    
    # Convert the result back to an image
    output_image = Image.fromarray(output_image_np)
    
    # Check and convert to RGB if necessary
    if output_image.mode == 'RGBA' and input_image.format.lower() == 'jpeg':
        output_image = output_image.convert('RGB')
    
    return output_image

st.title("Background Removal App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    input_image = Image.open(uploaded_file)
    
    # Remove the background
    output_image = remove_background(input_image)
    
    # Display the original and output images
    st.image(input_image, caption="Original Image", use_column_width=True)
    st.image(output_image, caption="Background Removed", use_column_width=True)

    # Download link for the output image
    buf = io.BytesIO()
    output_image.save(buf, format=input_image.format)
    byte_im = buf.getvalue()
    
    mime_type = f"image/{input_image.format.lower()}"
    st.download_button(label="Download Image", data=byte_im, file_name=f"output_image.{input_image.format.lower()}", mime=mime_type)
