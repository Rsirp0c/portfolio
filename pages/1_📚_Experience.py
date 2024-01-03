import streamlit as st
import streamlit.components.v1 as components
from constant import *

st.set_page_config(page_title="Experience", page_icon="📚", layout="wide")
st.header("📚 Experience",divider='rainbow')
st.write("")

def experience_unit(title, position, date, location, content):
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.subheader(title)
    with col3:
        st.write("")
        st.markdown("######   " + date)
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.markdown("###### " + position)
    with col3:
        st.markdown("######   " + location)
    st.write(content)

# Zbyte Technology ----------------------------------------------------------------
experience_unit(":blue[Zbyte] Technology | Data Warehouse Startup", "Product Manager Intern", 
                "May 2023 – Sep 2023", "Hangzhou, China", 
                """
                - Designed a **LLM - Dataset** chat app’s architecture with PM director, in which user could upload private datasets enabling LLM chat app response more accurately to domain-specific inquiries.
                - Maintained and fixed 150+ detailed errors in reusable **React** components for a web-base Data Warehouse while communicate with UI designers for ”designer review”.
                - Drafted and perfected the documentation for a Data Warehouse, including Data Types, 50+ SQL Commands, and 10+ Build-in Functions.
                - Published 3 articles, each attracts 5k+ reads for the company‘s tech blog; including two Analysis of Forrester and G2’s review on Cloud Data Warehouse.
                """)
st.link_button("Company website", "https://relyt.cloud")

st.divider()

# Branda ----------------------------------------------------------------
experience_unit(":violet[Branda] | Brandeis Campus App", "Software Engineer", 
                "Jan 2023 – present", "Waltham, MA", 
                """
                - Collaborated in a **Agile** software development cycle, main responsible for improving the mobile UI/UX.
                - Implemented a interactive calendar daily used by 1.6K student to keep track of school events, using **REST APIs** with **React Native** as the front-end. Utilized **Redis** to cache hotspot data, reducing the workload on main database.
                - Managed database migration from Heroku to **Firebase** to meet user growth, implemented API touchpoints within the CI/CD pipeline for migration testing.
                """)
st.link_button("App Store link", "https://apps.apple.com/us/app/branda/id1437022581")

st.divider()

# Quant Club ----------------------------------------------------------------
experience_unit("Brandeis :orange[Quant Club]", "Software Engineer", 
                "Jan 2023 – Sep 2023", "Waltham, MA", 
                """
                - Contribute to research, gather, and analyze information of different companies where we show users companies’ volatility indices using Python.
                - Designed and developed a website that allows users to see data regarding companies’ volatility indices utilizing **JavaScript, React, and Node.js** (setting up the website’s skeleton, capable of automatically giving users the most up-to-date information).
                """)
st.link_button("Club website", "https://brandeisquantclub.org")

st.divider()
# Research Assistant ----------------------------------------------------------------
experience_unit(":orange[Brandeis University] | Anthropology Department", "Research Assistant", 
                "Sep 2022 – Aug 2023", "Waltham, MA", 
                """
                - Collaborated with Anthropology professor Elizabeth Ferry on researching asset tokenization and cryptocurrencies as cultural phenomena.
                - Interviewed 17 people who worked in Finance and IT industry during the summer; asking about their opinion on Gold Tokenization, Bitcoin, Blockchain, and Central Bank digital Currency in China. These finding support and enrich Professor Ferry’s ongoing book writing about Gold in mining and finance.
                - Weekly report based on searching for and reading news, social media reports, and journalistic and academic analyses.
                """)
st.link_button("Department website", "https://www.brandeis.edu/anthropology/undergraduate/research-and-funding/student-bios.html")



