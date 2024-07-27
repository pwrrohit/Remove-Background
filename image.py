import streamlit as st
from PIL import Image, ImageFilter
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
    
    # Ensure the output image is in RGBA mode
    if output_image.mode != 'RGBA':
        output_image = output_image.convert('RGBA')
    
    return output_image

def apply_filter(image, filter_type):
    if filter_type == 'Smooth':
        return image.filter(ImageFilter.SMOOTH_MORE)
    elif filter_type == 'Blur':
        return image.filter(ImageFilter.GaussianBlur(radius=2))
    elif filter_type == 'Edge Enhance':
        return image.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_type == 'Sharpen':
        return image.filter(ImageFilter.SHARPEN)
    else:
        return image

def get_image_bytes(image, format):
    buf = io.BytesIO()
    image.save(buf, format=format)
    return buf.getvalue()

st.title("Background Removal and Enhancement App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "bmp", "tiff", "gif"])

if uploaded_file is not None:
    # Read the image
    input_image = Image.open(uploaded_file)
    
    # Remove the background
    output_image = remove_background(input_image)
    
    # Provide filter options
    filter_option = st.selectbox(
        "Choose a filter to apply:",
        ["None", "Smooth", "Blur", "Edge Enhance", "Sharpen"]
    )
    
    # Apply the selected filter
    output_image = apply_filter(output_image, filter_option)
    
    # Display the original and output images
    st.image(input_image, caption="Original Image", use_column_width=True)
    st.image(output_image, caption="Processed Image", use_column_width=True)

    # Provide format selection
    format_option = st.selectbox(
        "Choose the file format to save as:",
        ["PNG", "WEBP"]
    )
    
    # Get the image bytes in the selected format
    image_bytes = get_image_bytes(output_image, format_option)
    
    # Download link for the output image
    st.download_button(
        label=f"Download Image as {format_option}",
        data=image_bytes,
        file_name=f"output_image.{format_option.lower()}",
        mime=f"image/{format_option.lower()}"
    )
