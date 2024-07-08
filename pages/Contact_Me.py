import streamlit
from send_gmail import send_mail

with streamlit.form(key="email_form"):
    user_mail = streamlit.text_input("Your Email Address")
    raw_message = streamlit.text_area("Your Message")
    message = f"""\
    Subject: New mail from {user_mail}
    From: {user_mail}
    
    {raw_message}
    """
    button = streamlit.form_submit_button("Submit")
    if button:
        send_mail(message)
        print("Your mail is sent successfully!")