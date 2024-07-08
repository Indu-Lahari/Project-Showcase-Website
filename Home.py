import streamlit
import pandas

streamlit.set_page_config(layout="wide")

col1, col2 = streamlit.columns(2)

with col1:
    streamlit.image("images/photo.jpg", width=400)

with col2:
    streamlit.header("Indu Lahari")
    content = """Hey! I am Indu Lahari. I am a recent graduate from Aurora's Technological and Research Institute, Hyderabad.
                 Well, this website is designed to showcase my Python Programming skills."""
    streamlit.info(content)

content2 = streamlit.write("Below you can find some of the Python Apps I have created. Feel free to contact me!")

df = pandas.read_csv("data.csv", sep=";")

col3, empty_col, col4 = streamlit.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        streamlit.header(row["title"])
        streamlit.write(row["description"])
        streamlit.image("images/" + row["image"])
        streamlit.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        streamlit.header(row["title"])
        streamlit.write(row["description"])
        streamlit.image("images/" + row["image"])
        streamlit.write(f"[Source Code]({row['url']})")