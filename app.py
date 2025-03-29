from PIL import Image
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os
import textwrap
import pathlib

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# AI Prompt for Software Design Analysis
prompt = '''
Act as a Software Architect & Generate Bullet Point Answers in Crisp One to Two Lines Max.
Based on the provided software architecture diagram, analyze the following aspects:
1. Identify any potential flaws or inefficiencies in the architecture.
2. Assess adherence to best practices such as SOLID principles, Clean Architecture, and Microservices.
3. Suggest improvements in modularity, scalability, and maintainability.
4. Identify security vulnerabilities and recommend mitigations.
5. Evaluate technology stack and suggest alternative frameworks/languages if needed.
6. Analyze API structure and suggest improvements for efficiency and interoperability.
7. Assess scalability and performance under high-load conditions.
8. Recommend DevOps strategies for CI/CD, monitoring, and automated testing.
9. Identify bottlenecks in data flow and suggest optimization techniques.
10. Determine if the architecture follows industry standards and compliance guidelines.
If the User is uploading image on the topics other than software design related then respond with - "I am a Software Design Assistant Chatbot
and can analyse only sofware design related images"
'''

##If the User uploaded software architecture design related image do not have sufficient information for you to analyze, please respond with - "The 
##uploaded image does not have sufficient detail for me to clearly analyze the design. Please add more details in the image and re upload"

def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-2.0-flash')
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit UI
st.header("🖥️ Software Design Review Assistant")
st.subheader("🔍 AI-Powered Architecture Analysis", divider=True)

with st.expander("About this Application"):
    st.markdown("""
    This tool provides AI-driven insights for analyzing software architecture diagrams. 
    - **Design Evaluation**: Detects inefficiencies, security vulnerabilities, and scalability issues.
    - **Best Practice Adherence**: Checks compliance with SOLID, Clean Architecture, and other principles.
    - **Technology Recommendations**: Suggests frameworks, languages, and DevOps strategies.
    - **Performance Insights**: Evaluates system efficiency under various conditions.
    """)

# Sidebar for Image Upload
st.sidebar.title("Upload Software Architecture Diagram")
uploaded_file = st.sidebar.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

img = ""
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.sidebar.image(img, caption="Uploaded Architecture Diagram", use_container_width=True)

analyze_button = st.sidebar.button("Analyze Design")

# Perform AI Analysis
if analyze_button:
    response = get_gemini_response(prompt, img)
    st.subheader("📊 AI Analysis Report")
    st.write(response)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee;">
<p>Software Design Review Assistant - Prototype Version 1.0</p>
</div>
""", unsafe_allow_html=True)
