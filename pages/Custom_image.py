import streamlit as st
import cv2
import numpy as np
from PIL import Image


def create_flower_image(width, height):
    
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    
    green = (0, 255, 0)
    yellow = (0, 255, 255)
    red = (0, 0, 255)
    
    
    cv2.line(image, (width // 2, height), (width // 2, height // 2), green, thickness=5)
    
    
    petal_radius = 50
    center = (width // 2, height // 2)
    angles = [0, 72, 144, 216, 288]
    for angle in angles:
        x = int(center[0] + petal_radius * np.cos(np.deg2rad(angle)))
        y = int(center[1] + petal_radius * np.sin(np.deg2rad(angle)))
        cv2.circle(image, (x, y), petal_radius, red, -1)
    
    
    cv2.circle(image, center, petal_radius // 2, yellow, -1)
    
    return image


def main():
    st.title('Custom Flower Image Generator')
    st.write('This app generates a custom flower image using OpenCV and displays it using Streamlit.')

    
    flower_image = create_flower_image(512, 512)
    
    
    flower_image_rgb = cv2.cvtColor(flower_image, cv2.COLOR_BGR2RGB)
    

    st.image(Image.fromarray(flower_image_rgb), caption='Custom Flower Image', use_column_width=True)


if __name__ == '__main__':
    main()
