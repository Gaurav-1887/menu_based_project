import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st

def send_bulk_email(email_sender, email_subject, email_body, email_recipients):
    email_password = "xexprxohdbnjhaxb"  # Fixed password
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    context = smtplib.SMTP(smtp_server, smtp_port)
    context.starttls()
    context.login(email_sender, email_password)

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = ', '.join(email_recipients)
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_body, 'plain'))

    context.sendmail(email_sender, email_recipients, msg.as_string())
    st.success("Email sent successfully!")

    context.quit()

def main():
    st.title("Bulk Email Sender")

    email_sender = st.text_input("Enter your Email Address:")
    email_subject = st.text_input("Enter Email Subject:")
    email_body = st.text_area("Enter Email Body:")

    email_recipients = st.text_area("Enter Recipients' Email Addresses (comma-separated):")
    if email_recipients:
        email_recipients = [email.strip() for email in email_recipients.split(',')]

    if st.button("Send Email"):
        if email_sender and email_subject and email_body and email_recipients:
            send_bulk_email(email_sender, email_subject, email_body, email_recipients)
        else:
            st.warning("Please fill in all the fields.")

if __name__ == "__main__":
    main()
