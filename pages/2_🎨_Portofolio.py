from constant import *
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="Portofolio", page_icon="🎨", layout="wide")

st.header("🎨 Portfolio",divider='rainbow')

# Deis Evaluation ----------------------------------------------------------------
st.subheader(":blue[Deis]Evaluation - Course Evaluation Website", divider="grey") 
st.write("""
        Launched a course evaluation web app for Brandeis students to review and share courses, exceeding 200+ active users.
        Designed the whole UI with Figma and Implemented front end with Javascript, HTML/CSS in a MERN Stack.
        """)
tab1, tab2 = st.tabs(["UI/UX", "View Website"])
with tab1:
#    st.subheader("UI/UX design")
   components.iframe(figma_link, width=800, height=500, scrolling=True)
with tab2:
#    st.subheader("View Website")
   st.link_button("Go to Website", "https://deis-evaluation.onrender.com")
   components.iframe("https://deis-evaluation.onrender.com", width=800, height=600, scrolling=True)

# Data VIS in D3.js --------------------------------------------------------------
st.subheader("Data Visualization in :orange[D3.js]",divider='grey')
st.write("""
        Created a data visualization web app for Massachusetts police expenditure data using D3.js.
        """)
st.link_button("Go to Github", "https://github.com/Rsirp0c/D3-practice")

st.image("src/Screenshot-2.png", width=800)
with st.expander("See more"):
   st.image("src/Screenshot-1.png", width=800)
   st.image("src/Screenshot-3.png", width=800)
   st.image("src/Screenshot-4.png", width=800)

# Desktop ChatApp -------------------------------------------------------------- 
st.subheader(":blue[LLM] Desktop ChatApp",divider='grey')
st.write("""
        Designed and developed a cross-platform **desktop LLM Chat app**, enabling chat over user-upload dataset; providing a
        more accurate response to domain-specific inquiries than ChatGPT.
        """)
st.write("""
        Utilized Embedding and Searching from **OpenAI API** to optimize Chat app’s response. Split the user-upload file into
        small chunks; used OpenAI Embedding model to vectorize each chunk and save them into Qdrant database. Transform
        user query to vector using OpenAI, and then inquire the top match text chunk from Qdrant database using topk value.
        """)
st.link_button("Go to :blue[Source Code]", "https://github.com/Rsirp0c/desktop_chatapp")

# Anthropology Research Project -----------------------------------------------------------
st.subheader(":orange[Anthropology] Research Project - A Timeless Building",divider='grey')   
st.write("""
        An **qualitative anthropological research** on the preservation and adaption of historical sites; 
        as final project, received the highest score in class.
        """)
st.write("""
        My fieldwork includes interviewing educators, examing archive, on-site obervation. 
        Through my fieldwork at King’s Chapel, I argued for a humane approach to preserving historic sites, 
        that seeks a balance between **maintaining the historical significance and the sites’ adaptations to societal changes**.
        """)
components.iframe(StoryMap_iframe, width=1000, height=700, scrolling=True)
