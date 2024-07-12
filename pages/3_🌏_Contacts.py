import streamlit as st 
from constant import *

st.set_page_config(page_title="Contacts", page_icon="🌏",initial_sidebar_state="collapsed",layout="wide") #
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu()

    st.markdown(f"##### 📞 Phone: +1 {phone}")   
    st.markdown(f"##### ✉️ Email: {email}")
    with st.container():
        col1, col2 = st.columns([0.1, 3])
        with col1:
            st.write(linkedin_logo, unsafe_allow_html=True)
        with col2:
            st.markdown(f"#####  Linkedin: {linkedin_link}")
    with st.container():
        col1, col2 = st.columns([0.1, 3])
        with col1:
            st.write(github_logo, unsafe_allow_html=True)
        with col2:
            st.markdown(f"#####  Github: {github_link}")



