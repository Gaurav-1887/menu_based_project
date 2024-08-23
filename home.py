import streamlit as st

# Add CSS for gradient background (orange gradient)
css = """
<style>
html, body {
    height: 100%;
    margin: 0;
}

body {
    background-color: #f0f0f0; /* fallback for non-webkit browsers */
    background-image: linear-gradient(to right, #f76c6c, #f76c6c, #fbc7a6);
    background-image: -webkit-linear-gradient(to right, #f76c6c, #f76c6c, #fbc7a6);
    font-family: Arial, sans-serif;
}

.stApp {
    background-color: transparent !important;
}
</style>
""" 

# Render the HTML/CSS for background
st.markdown(css, unsafe_allow_html=True)

# Streamlit components
st.title("Hello, Welcome to Menu Based Project")
st.write("Please navigate to the sidebar for utilizing different services.")
