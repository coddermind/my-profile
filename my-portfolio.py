import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Muhammad Abrar's Portfolio", page_icon="📊", layout="wide")

# Hide the three dots menu and Streamlit footer
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Custom CSS for background color and font color
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
    }
    .css-18e3th9 {
        background-color: black;
    }
    .stTextInput > div > div > input {
        color: white;
    }
    .css-1q8dd3e {
        color: white;
    }
    .stButton button {
        color: white;
        background-color: #4CAF50;
    }
    .css-10trblm, .css-1d391kg, .css-16huue1, .css-2trqyj, .css-hxt7ib {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Create a two-column layout for the title and profile image
col1, col2 = st.columns([3, 1])  # Adjusting the width ratio for text and image

# Left column for title and introduction
with col1:
    st.title("Muhammad Abrar's Portfolio")
    st.subheader("Student of BS Artificial Intelligence at Superior University")
    st.write("""
    Welcome to my portfolio! I am Muhammad Abrar, an AI enthusiast with expertise in Artificial Intelligence, 
    Data Science, and Web Development. I have developed various projects in machine learning, deep learning, data science, 
    and web applications using Django. Below are some of the key projects I've worked on and my areas of expertise.
    """)

# Right column for profile image
with col2:
    st.image("images/profile_image.png", width=150, caption="Muhammad Abrar", use_container_width=True)

# Projects Section
st.header("Projects & Expertise")

st.subheader("1. Artificial Intelligence and Machine Learning")
st.write("""
- *Data Analysis & Visualization*: Extensive experience in analyzing datasets and visualizing trends using Pandas, Matplotlib, and Seaborn. Here is a 3-months detailed sales analysis and visualization of a store. [View Demo](https://drive.google.com/file/d/1VzCVgJQyPIpBDLLuhF2CHiVFSEPiOIIQ/view?usp=sharing)
- *Machine Learning Model Integration*: Integration of ML models into applications, focusing on automation and prediction accuracy. [View Demo Video](https://drive.google.com/file/d/1i6d6ldDw7Bo7A3xRZuWrv1oS7DZK4rYa/view?usp=sharing)
- *CNN for Gender Recognition*: Built a Convolutional Neural Network (CNN) to classify gender based on image datasets.
- *YOLO Object Detection Model*: Developed an object detection model using YOLO, improving accuracy in live video feeds and image datasets.
""")

st.subheader("2. Web Development")
st.write("""
- *E-commerce Website (Django)*: Developed a complete e-commerce website using Django with features such as product management, user authentication, and payment processing. [View Demo](https://codder.pythonanywhere.com/)
- *MultiVendor E-commerce Plateform*: Developed a complete multi-vendor e-commerce plateform using Django with features such as seller and buyer account management, product management, order management, order history, email system, user authentication, and payment processing. [View Demo](https://alnamaa.pythonanywhere.com/)
- *School Management System*: Developed a complete school management system with separate portals for admins, teachers, and students. All the important functionalities can be performed on the portal; such as Assigning subjects, Timetable creation, fees, salaries, attendance, assignments etc. For demo the teacher login credentials are Email: teacher1@school.com to teacher6@school.com, Password: teacher123. For demo student login: Email: student1@school.com to student9@school.com, Password: student123. The admin Login credentials cannot be provided here. [View Demo](https://realworkfinancingbroker.pythonanywhere.com/)
- *PDF Reader with Gemini API*: Created a PDF reader using the Gemini API for text extraction and advanced querying. [View Demo](https://pdf-question-answer-chatbot.streamlit.app/)
- *Django Projects*: Built multiple full-stack web applications using Django for both frontend and backend functionalities.
""")

st.subheader("3. Data Science & Automation")
st.write("""
- *Data Scraping Projects*: Scraped data from websites using Selenium and BeautifulSoup for building datasets. [View Demo of priceoye scraping](https://priceoye-scrapper.streamlit.app/)
- *Data Preprocessing & Modeling*: Proficient in cleaning, transforming, and scaling data to improve machine learning model performance.
""")

st.subheader("4. Miscellaneous Python Tasks")
st.write("""
- *File Conversions*: Automated file conversions (PDF, Excel, Word) and other formats.
- *QR/Barcode Generation*: Developed tools to generate and scan QR codes and barcodes.
- *Video/Image Processing*: Converted between images and videos, and extracted frames from videos.
- *YouTube/Facebook Video Downloader*: Created tools to download videos from YouTube and Facebook.
""")

# Skills Section
st.header("Skills")
st.write("""
- *Artificial Intelligence (AI)*
- *Data Visualization*
- *Data Science*
- *Object Detection*
- *Machine Learning & Deep Learning*
- *Natural Language Processing (NLP)*
- *Computer Vision*
- *Data Science & Analysis*
- *Data Visualization*
- *Web Development (Django)*
- *API Integration*
- *Cloud Application Development*
- *Data Scraping*
""")

# Certifications Section with Images
st.header("Certifications")

st.subheader("1. Microsoft Azure AI Fundamentals")
st.write("""
Certified in Microsoft Azure AI Fundamentals, demonstrating knowledge in AI services and tools provided by Azure. [View Certification](https://drive.google.com/file/d/16Jx12eOJ3wV4p8GdMjHBhT8yIgKefgT1/view?usp=sharing)
""")

st.subheader("2. Artificial Intelligence from Corvit")
st.write("""
Certified in Artificial Intelligence from Corvit, covering core AI concepts, machine learning, and deep learning techniques. [View Certificate](https://drive.google.com/file/d/13QKpvug1A1PLVuhALWulazVMxnSZxzGX/view?usp=sharing)
""")

st.subheader("3. Artificial Intelligence from Akhuwat")
st.write("""
Certified in Artificial Intelligence from Akhuwat, including various AI models, data preprocessing, and real-world applications. [View Certificate](https://drive.google.com/file/d/1MmAnDcG6vsLCt6zKeLfZx82MocXRqFdF/view?usp=sharing)
""")

# Contact Information Section
st.header("Contact")
st.write("Feel free to reach out to me for collaboration or inquiries!")

st.write("*Email*: [hacodder@gmail.com](mailto:hacodder@gmail.com)")
st.write("*Phone*: [+923065516830](tel:+923065516830)")
st.write("*WhatsApp*: [923065516830](https://wa.me/923065516830)")
st.write("*GitHub*: [github.com/coddermind](https://github.com/coddermind)")
st.write("*LinkedIn*: [Muhammad Abrar on LinkedIn](https://www.linkedin.com/in/muhammad-abrar-b1508a357)")

# Footer
st.write("Thank you for visiting my portfolio!")
