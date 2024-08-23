import streamlit as st
import pyautogui as py
import time

def send_sms():
    st.title("Send SMS via Mobile Automation")

    phone = st.text_input("Enter the phone number or name (If number exists in contact list):")
    msg = st.text_area("Type your message here:")

    if st.button("Send SMS"):
        st.info("Opening Phone Link. Please ensure your phone is connected and linked.")
        py.press('win')
        time.sleep(3)
        py.typewrite("Phone Link")
        time.sleep(5)
        py.press('enter')
        time.sleep(8)  

        message = py.locateOnScreen(r"C:\Users\gaura\OneDrive\Desktop\message.png")
        time.sleep(2)
        py.click(message)
        time.sleep(2)

        compose = py.locateOnScreen(r"C:\Users\gaura\OneDrive\Desktop\compose.png")
        time.sleep(2)
        py.click(compose)
        time.sleep(2)

        py.typewrite(phone)
        time.sleep(2)
        py.press('enter')
        time.sleep(2)

        send = py.locateOnScreen(r"C:\Users\gaura\OneDrive\Desktop\Screenshot 2024-06-25 161259.png")
        time.sleep(3)
        py.click(send)
        time.sleep(3)
        py.click(send)
        time.sleep(2)

        py.typewrite(msg)
        time.sleep(1)
        py.press('enter')

        st.success("Your message has been sent successfully.")

if __name__ == "__main__":
    send_sms()
