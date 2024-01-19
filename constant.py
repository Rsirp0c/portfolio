skill_col_size = 5

#publication_url --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                           
'''

# personal info (for main page) --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
info = {'brief':
              """    
                Starting from physical therapist, to UX designer, to software engineer and product manager... 
                I am a passionate and curious explorer currently pursuing a Computer Science and Anthropology major at Brandeis University, expected to graduate in May 2025.
                **I believe in the intersectionality of quantitative and qualitative subjects, that neither approach alone can lead one to the absolute truth.**
              """,
        'name':'Haoran cheng', 
        'study':'Brandeis University',
        'location':'Boston, MA',
        'interest':'Full Stack, Data Science, Product Management',
        'skills':['Python','Java','Javascript','Typescript','Shell','HTML & CSS','React','Node.js','Tableau','Streamlit','PySpark','Svelte','Docker','Kafka','Kubernetes','MongoDB','PostgreSQL','MySQL','SQLite','AWS','Github','Gitlab','Figma','OpenAI API','Excalidraw','Trello','REST api','HTTP'],
        }

# Experience --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#[[header, subheader, date, location, content, link, link_url], [...], etc.]

Experience = [
              [":blue[Zbyte] Technology | Data Warehouse Startup", "Product Manager Intern", 
              "May 2023 – Sep 2023", "Hangzhou, China", 
              """
              - Designed a **LLM - Dataset** chat app’s architecture with PM director, in which user could upload private datasets enabling LLM chat app response more accurately to domain-specific inquiries.
              - Maintained and fixed 150+ detailed errors in reusable **React** components for a web-base Data Warehouse while communicate with UI designers for ”designer review”.
              - Drafted and perfected the documentation for a Data Warehouse, including Data Types, 50+ SQL Commands, and 10+ Build-in Functions.
              - Published 3 articles, each attracts 5k+ reads for the company‘s tech blog; including two Analysis of Forrester and G2’s review on Cloud Data Warehouse.
              """,
              "Company website", "https://relyt.cloud"],

              [":violet[Branda] | Brandeis Campus App", "Software Engineer", 
                "Jan 2023 – present", "Waltham, MA", 
                """
                - Collaborated in a **Agile** software development cycle, main responsible for improving the mobile UI/UX.
                - Implemented a interactive calendar daily used by 1.6K student to keep track of school events, using **REST APIs** with **React Native** as the front-end. Utilized **Redis** to cache hotspot data, reducing the workload on main database.
                - Managed database migration from Heroku to **Firebase** to meet user growth, implemented API touchpoints within the CI/CD pipeline for migration testing.
                """,
                "App Store link", "https://apps.apple.com/us/app/branda/id1437022581"],

              ["Brandeis :orange[Quant Club]", "Software Engineer", 
                "Jan 2023 – Sep 2023", "Waltham, MA", 
                """
                - Contribute to research, gather, and analyze information of different companies where we show users companies’ volatility indices using Python.
                - Designed and developed a website that allows users to see data regarding companies’ volatility indices utilizing **JavaScript, React, and Node.js** (setting up the website’s skeleton, capable of automatically giving users the most up-to-date information).
                """,
              "Club website", "https://brandeisquantclub.org"],

              [":orange[Brandeis University] | Anthropology Department", "Research Assistant",
                "Sep 2022 – Aug 2023", "Waltham, MA", 
                """
                - Collaborated with Anthropology professor Elizabeth Ferry on researching asset tokenization and cryptocurrencies as cultural phenomena.
                - Interviewed 17 people who worked in Finance and IT industry during the summer; asking about their opinion on Gold Tokenization, Bitcoin, Blockchain, and Central Bank digital Currency in China. These finding support and enrich Professor Ferry’s ongoing book writing about Gold in mining and finance.
                - Weekly report based on searching for and reading news, social media reports, and journalistic and academic analyses.
                """,
                "Department website", "https://www.brandeis.edu/anthropology/undergraduate/research-and-funding/student-bios.html"]
              ]      

# Portfolio --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#     {'project1':[HEADER, CONTENT]
#      'project2':[HEADER, CONTENT]
#      ...}

Portfolio = { 1:[':blue[Deis]Evaluation - Course Evaluation Website',
              """
              Launched a course evaluation web app for Brandeis students to review and share courses, exceeding 200+ active users.
              Designed the whole UI with Figma and Implemented front end with Javascript, HTML/CSS in a MERN Stack.
              """],
              2:['Data Visualization in :orange[D3.js]',
                  """
                Created a data visualization web app for Massachusetts police expenditure data using D3.js.
                """],
              3:[':blue[LLM] Desktop ChatApp',
                """
                - Designed and developed a cross-platform **desktop LLM Chat app**, enabling chat over user-upload dataset; providing a more accurate response to domain-specific inquiries than ChatGPT.
                - Utilized Embedding and Searching from **OpenAI API** to optimize Chat app’s response. Split the user-upload file into small chunks; used OpenAI Embedding model to vectorize each chunk and save them into Qdrant database. Transform user query to vector using OpenAI, and then inquire the top match text chunk from Qdrant database using topk value.
                """],
              4:[':orange[Anthropology] Research Project - A Timeless Building',
                """
                - An **qualitative anthropological research** on the preservation and adaption of historical sites; as final project, received the highest score in class.
                - My fieldwork includes interviewing educators, examing archive, on-site obervation. Through my fieldwork at King’s Chapel, I argued for a humane approach to preserving historic sites, that seeks a balance between **maintaining the historical significance and the sites’ adaptations to societal changes**.
                """]
            }
              
# Contacts --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
phone = "971-900-6780"
email = "haorancheng@brandeis.edu"
linkedin_link = "www.linkedin.com/in/haoran-cheng-018b9318b/"
github_link = "https://github.com/Rsirp0c?tab=repositories"


# iframes --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
figma_iframe = '<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1" allowfullscreen></iframe>'

figma_link = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1"

StoryMap_iframe = "https://storymaps.arcgis.com/stories/dfb9689618e343cf9f6ef36d9a8329a7?header"

Evaluation_html = '''
                <div class="github-card" data-github="Rsirp0c/deis-course-evaluation" data-width="400" data-height="" data-theme="default"></div>
                <script src="https://cdn.jsdelivr.net/github-cards/latest/widget.js"></script>                
                '''
