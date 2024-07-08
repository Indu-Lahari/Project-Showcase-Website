import streamlit

with streamlit.form(key="email_form"):
    streamlit.text_input("Your Email Address")
    streamlit.text_area("Your Message")
    button = streamlit.form_submit_button("Submit")
    if button:
        print("Your mail is sent successfully!")