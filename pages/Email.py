import streamlit as st
from email.message import EmailMessage
import ssl
import smtplib

def send_email(email_sender, email_receiver, subject, body):
    email_password = "xexprxohdbnjhaxb"  # Fixed password

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    return "Email was sent successfully"

# Streamlit app title
st.title("Email Sender")

# Input fields for email details
email_sender = st.text_input("Enter your email:")
email_receiver = st.text_input("Enter the recipient's email:")
subject = st.text_input("Enter the email subject:")
body = st.text_area("Enter the email body:")

# Button to send the email
if st.button("Send Email"):
    if email_sender and email_receiver and subject and body:
        result = send_email(email_sender, email_receiver, subject, body)
        st.success(result)
    else:
        st.error("Please fill in all fields.")
