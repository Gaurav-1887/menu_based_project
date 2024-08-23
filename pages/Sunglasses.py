import streamlit as st
import cv2
import numpy as np

def detect_faces_and_eyes(frame, overlay_image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = gray_img[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) > 0:
            ex_min, ey_min = eyes[0][:2]
            ex_max, ey_max = eyes[0][:2]
            ew_max, eh_max = eyes[0][2:]

            for (ex, ey, ew, eh) in eyes:
                ex_min = min(ex_min, ex)
                ey_min = min(ey_min, ey)
                ex_max = max(ex_max, ex + ew)
                ey_max = max(ey_max, ey + eh)

            overlay_width = ex_max - ex_min
            overlay_height = ey_max - ey_min

            resized_overlay = cv2.resize(overlay_image, (overlay_width, overlay_height))

            # Check if the overlay fits within the ROI bounds
            if ey_min + overlay_height <= roi_color.shape[0] and ex_min + overlay_width <= roi_color.shape[1]:
                roi_color[ey_min:ey_min+overlay_height, ex_min:ex_min+overlay_width] = resized_overlay

    return frame

def main():
    st.title('Real-Time Face and Eye Detection with Sunglasses Overlay')

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("Error: Failed to open webcam.")
        return

    # Load sunglasses image once
    overlay_image = cv2.imread(r"C:\Users\gaura\OneDrive\Desktop\sunglasses.jpg")

    stframe = st.empty()  # Placeholder for video frames

    while True:
        ret, frame = cap.read()

        if not ret:
            st.error("Error: Failed to capture image from webcam.")
            break

        frame_with_overlay = detect_faces_and_eyes(frame, overlay_image)

        frame_rgb = cv2.cvtColor(frame_with_overlay, cv2.COLOR_BGR2RGB)

        stframe.image(frame_rgb, caption='Face and Eye Detection', use_column_width=True)

        # Adding a small delay to make the video smoother
        cv2.waitKey(1)

    cap.release()

if __name__ == '__main__':
    main()
