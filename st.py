
import streamlit as st

st.set_page_config(
    page_title="Premalu",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(90deg, #8b5cf6, #d946ef);
}

h1 {
    text-align: center;
    color: white;
}

.stButton > button {
    background: linear-gradient(90deg, #EEAECA, #94BBE9);
    color: #222;
    border: none;
    border-radius: 20px;
    padding: 10px 25px;
    transition: 0.3s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #94BBE9, #EEAECA);
    color: black;
    border: none;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

st.title("Premalu")

left, center, right = st.columns([1, 2, 1])

with center:
    if st.button("Click me", use_container_width=True):
      st.video(r"Premalu.mkv")