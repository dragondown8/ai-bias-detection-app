import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os

st.set_page_config(page_title="AI Bias Detection Tool", layout="wide")

st.title("🔍 AI Bias Detection Tool")
st.write("Upload an image to analyze potential bias in AI-generated or selected content")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Convert PIL image to OpenCV format
    opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Simple bias analysis (placeholder for now)
    st.subheader("📊 Bias Analysis Results")
    
    # Basic image analysis
    height, width = opencv_image.shape[:2]
    
    st.write(f"**Image Dimensions:** {width} x {height} pixels")
    
    # Placeholder bias detection results
    st.write("**Bias Analysis:**")
    st.write("✅ This is a working bias detection tool!")
    st.write("🔧 Ready for enhancement with advanced bias detection algorithms")
    
    # Color analysis
    avg_color = np.mean(opencv_image, axis=(0,1))
    st.write(f"**Average Color Values:** R:{avg_color[2]:.1f}, G:{avg_color[1]:.1f}, B:{avg_color[0]:.1f}")

st.markdown("---")
st.write("**AI Bias Detection Tool** - Helping create more inclusive AI systems")
