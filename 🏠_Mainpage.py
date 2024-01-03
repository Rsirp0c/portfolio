import streamlit as st
import streamlit.components.v1 as components
from constant import *

st.set_page_config(page_title="Main Page", page_icon="🏠", layout="wide") 

#sidebar
st.sidebar.success("Select a page above.")

# Add the badge to the sidebar
# with st.sidebar:
# components.html(linkedin_badge_html, height=200)

#main page
st.header("About Me",divider='rainbow')

col1, col2, col3 = st.columns([1.3 ,0.2, 1])

with col1:
    st.write(
    ' Starting from physical therapist, to UX designer, to software engineer and product manager... ' +
    'I am a passionate and curious explorer currently pursuing a Computer Science and Anthropology major at Brandeis University, expected to graduate in May 2025. ' +
    '**I believe in the intersectionality of quantitative and qualitative subjects, that neither approach alone can lead one to the absolute truth.**'
    )
    st.markdown("###### 😄 Name: Haoran Cheng, just call me Harry!")
    st.markdown("###### 👉 Study: Brandeis University")
    # st.markdown("#### 🇨🇳 Nationality: Chinese")
    st.markdown("###### 📍 Location: Boston, MA")
    st.markdown("###### 🏄 Interest: Full Stack, Data Science, Product Management")
    st.markdown("###### 🟡 Favorite Color: Yellow")
    st.markdown("###### 👀 Linkedin: www.linkedin.com/in/haoran-cheng-018b9318b/")
    
    #st.divider()
    with open("src/resume.pdf", "rb") as file:
        pdf_file = file.read()

    st.download_button(
        label="Download my :blue[resume]",
        data=pdf_file,
        file_name="resume",
        mime="application/pdf")

with col3:
    st.image("src/portrait.jpeg", width=360)

st.subheader("My :blue[skills] ⚒️",divider='rainbow') #,divider='rainbow'

def skill_tab():
    rows,cols = len(info['skills'])//skill_col_size, skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()

# x = st.slider("Select a value")
# st.markdown(f"# {x} squared is {x * x}")
