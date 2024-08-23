import streamlit as st
import pyautogui as py
import webbrowser as wb
import time

def send_whatsapp(mob, message):
    whatsapp_url = f"https://web.whatsapp.com/send?phone={mob}"
    wb.open(whatsapp_url)
    
    # Inform the user to scan the QR code if not already logged in
    st.info("Please scan the QR code on WhatsApp Web if not already logged in.")
    
    # Give time for the user to scan the QR code and for the chat to load
    time.sleep(25)
    
    # After the page is loaded, send the message
    py.typewrite(message)
    py.press("enter")

st.title("WhatsApp Message Sender")

mobile_number = st.text_input("Enter the mobile number (with country code, e.g., +1234567890):")
message = st.text_area("Type the message:")

if st.button("Send Message"):
    if mobile_number and message:
        st.warning("Make sure your browser is focused on the WhatsApp Web tab.")
        send_whatsapp(mobile_number, message)
        st.success("Message sent successfully!")
    else:
        st.error("Please enter both the mobile number and the message.")
