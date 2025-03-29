# **Software Design Review Assistant**  

## **Overview**  
This repository contains an AI-powered tool for analyzing and providing structured feedback on software architecture diagrams, flowcharts, and system designs. It helps developers, architects, and engineers improve system efficiency, scalability, and maintainability using AI-driven insights.  

## **Purpose**  
The tool automates software design reviews, ensuring adherence to best practices, optimizing performance, and recommending technologies based on the provided architecture.  

📋 **Table of Contents**  
- Overview  
- Features  
- Installation  
- Usage  
- Configuration  
- Prompt Design  
- Technologies Used  
- Contributing  
- License  

## 🚀 **Features**  
- **Automated Design Evaluation** – Detects flaws, inefficiencies, and bottlenecks.  
- **Best Practices & Design Patterns** – Assesses alignment with architectural principles like MVC, Microservices, and DDD.  
- **Implementation Feasibility** – Highlights challenges in deployment and maintenance.  
- **Technology Recommendations** – Suggests suitable programming languages, frameworks, and tools.  
- **Scalability & Performance Insights** – Evaluates system efficiency under load.  
- **Security & Compliance Checks** – Identifies vulnerabilities and mitigation strategies.  
- **API & Integration Review** – Validates API structure, interoperability, and documentation.  
- **Code Quality & Maintainability** – Provides feedback on modularity, extensibility, and DevOps integration.  

## 🛠️ **Installation**  
To run the project locally, follow these steps:  

1. **Clone the repository:**  
   ```sh
   git clone https://github.com/subamdebnath739/software-design-review-assistant.git
   cd software-design-review-assistant
   ```  

2. **Create and activate a virtual environment:**  
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Linux/Mac
   .venv\Scripts\activate  # On Windows
   ```  

3. **Install required dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```  

4. **Set up the API key in a `.env` file:**  
   ```sh
   AI_API_KEY=your_openai_or_gemini_api_key_here
   ```  

## 🖥️ **Usage**  
Run the application using Streamlit:  
```sh
streamlit run app.py
```  

### **How to Use**  
1. Upload a **software architecture diagram** (JPG, PNG, SVG).  
2. Click **"Analyze Design"** to receive structured AI-generated feedback.  
3. Review insights on **bottlenecks, implementation challenges, security risks, and recommended improvements.**  

## ⚙️ **Configuration**  
- Edit `.env` file to add API keys for AI analysis.  
- Modify `config.py` to adjust model parameters.  

## 📋 **Prompt Design**  
The AI is prompted with structured queries to evaluate software design based on:  
- **Clarity & Completeness:** Verifies if the architecture diagram effectively conveys system components and interactions.  
- **Design Patterns & Best Practices:** Checks alignment with SOLID principles, Clean Architecture, and Microservices.  
- **Scalability & Performance:** Evaluates load balancing, concurrency handling, and database optimization.  
- **Security & Compliance:** Identifies vulnerabilities in authentication, data security, and industry standards compliance.  
- **API & Integration Review:** Assesses API structure, documentation, and external system compatibility.  

## 🛠️ **Technologies Used**  
- **Python** – Core programming language.  
- **Streamlit** – Web framework for AI-driven design analysis.  
- **OpenAI / Gemini API** – AI-powered feedback generation.  
- **PIL** – Image processing for architecture diagrams.  
- **dotenv** – Secure management of API keys.  

## 🤝 **Contributing**  
- Contributions, issues, and feature requests are welcome!  
- Fork the repository and submit a pull request.  

## 📜 **License**  
This project is open-source and available under the **MIT License.**  
