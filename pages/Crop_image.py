import streamlit as st
import cv2
import numpy as np
from matplotlib import pyplot as plt

def crop_image():
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
        return

    
    ret, frame = cap.read()

    if not ret:
        st.error("Error: Could not read frame.")
        cap.release()
        return

    
    cap.release()

    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        st.warning("No faces detected.")
    else:
        
        for i, (x, y, w, h) in enumerate(faces):

            face_crop = frame[y:y+h, x:x+w]

            
            st.subheader(f"Cropped Face {i+1}")
            st.image(cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB))

           
            frame[0:h, 0:w] = face_crop

        st.subheader("Main Image with Cropped Faces")
        st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

def main():
    st.title("Face Detection and Cropping")
    st.write("This app detects faces in the webcam feed and crops them.")

    if st.button("Detect and Crop Faces"):
        crop_image()

if __name__ == "__main__":
    main()
