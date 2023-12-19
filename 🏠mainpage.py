import streamlit as st

st.set_page_config(page_title="Main Page",layout="wide") #page_icon="🏠",

st.header("About Me",divider='rainbow')

col1, col2, col3 = st.columns([1.3 ,0.1, 1])

with col1:
    st.write(
    '#### Starting from physical therapist, to UX designer, to software engineer and product manager... ' +
    'I am a passionate and curious explorer currently pursuing a Computer Science and Anthropology major at Brandeis University, expected to graduate in May 2025. ' +
    '**I believe in the intersectionality of quantitative and qualitative subjects, that neither approach alone can lead one to the absolute truth.**'
    )
    st.markdown("#### 👉S tudy: Brandeis University")
    # st.markdown("#### 🇨🇳 Nationality: Chinese")
    st.markdown("#### 📍 Location: Boston, MA")
    st.markdown("#### 🏄 Interest: Full Stack, Data Science, Product Management")
    st.markdown("#### 👀 Linkedin: www.linkedin.com/in/haoran-cheng-018b9318b/")
with col3:
    st.image("src/portrait.jpeg", width=400)
# x = st.slider("Select a value")
# st.markdown(f"# {x} squared is {x * x}")