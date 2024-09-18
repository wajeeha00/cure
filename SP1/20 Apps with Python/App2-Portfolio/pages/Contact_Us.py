import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="form1"):
    user_email = st.text_input(label="Email Address")
    raw_message = st.text_area(label="Your Message")
    button = st.form_submit_button(label="Submit")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}"""

    if button:
        send_email(message)
        st.info("Your Email was sent!")