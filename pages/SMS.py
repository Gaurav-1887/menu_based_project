import streamlit as st
from twilio.rest import Client

def send_sms(account_sid, auth_token, from_number, to_number, message_body):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        from_=from_number,
        to=to_number
    )
    return f"Message sent with SID: {message.sid}"

st.title("SMS Sender")

account_sid = st.text_input("Enter your Twilio Account SID:")
auth_token = st.text_input("Enter your Twilio Auth Token:", type="password")
from_number = st.text_input("Enter your Twilio phone number:")
to_number = st.text_input("Enter the recipient's phone number:")
message_body = st.text_area("Enter the message body:")

if st.button("Send SMS"):
    if account_sid and auth_token and from_number and to_number and message_body:
        result = send_sms(account_sid, auth_token, from_number, to_number, message_body)
        st.success(result)
    else:
        st.error("Please fill in all fields.")
