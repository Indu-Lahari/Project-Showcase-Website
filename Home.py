import streamlit

streamlit.set_page_config(layout="wide")

col1, col2 = streamlit.columns(2)

with col1:
    streamlit.image("images/photo.jpg", width=400)

with col2:
    streamlit.header("Indu Lahari")
    content = """Hey! I am Indu Lahari. I am a recent graduate from Aurora's Technological and Research Institute, Hyderabad.
                 Well, this website is designed to showcase my Python Programming skills."""
    streamlit.info(content)
