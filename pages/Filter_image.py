import streamlit as st
import cv2
import numpy as np

def display_images(original_image):
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    
    st.subheader("Original Image")
    st.image(original_image, channels="BGR")  
    
    st.subheader("Grayscale Image")
    st.image(gray_image, channels="GRAY")  


def main():
    st.title("Display Original and Grayscale Images")
    st.write("This app displays an original and grayscale version of an image.")

    
    uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        original_image = cv2.imdecode(file_bytes, 1)  

        if original_image is not None:
            display_images(original_image)
        else:
            st.error("Failed to load the uploaded image.")

if __name__ == "__main__":
    main()
