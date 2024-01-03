import streamlit as st 
import streamlit.components.v1 as components
from constant import *

st.set_page_config(page_title="Contacts", page_icon="🌏") #layout="wide"

st.markdown("##### 📞 Phone: +1 971-900-6780")   
# st.markdown("#### 🇨🇳 Nationality: Chinese")
st.markdown("##### ✉️ Email: haorancheng@brandeis.edu")
with st.container():
    col1, col2 = st.columns([0.1, 3])
    with col1:
        st.write(linkedin_logo, unsafe_allow_html=True)
    with col2:
        st.markdown("#####  Linkedin: www.linkedin.com/in/haoran-cheng-018b9318b/")
with st.container():
    col1, col2 = st.columns([0.1, 3])
    with col1:
        st.write(github_logo, unsafe_allow_html=True)
    with col2:
        st.markdown("#####  Github: https://github.com/Rsirp0c?tab=repositories")



