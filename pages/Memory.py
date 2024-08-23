import streamlit as st
import psutil

def read_ram():
    memory_info = psutil.virtual_memory()
    
    st.title("Memory Info")	
    st.write(f"Total: {memory_info.total / (1024 ** 3):.2f} GB")
    st.write(f"Available: {memory_info.available / (1024 ** 3):.2f} GB")
    st.write(f"Used: {memory_info.used / (1024 ** 3):.2f} GB")
    st.write(f"Percentage: {memory_info.percent}%")

read_ram()