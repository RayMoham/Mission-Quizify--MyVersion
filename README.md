# 📚 Gemini Quizify - (AI Quiz Builder) 📚

<div align="center">
  <br />
    <a>
      <img src="image.png" alt="Project Banner">
    </a>
  <br />

  <div>
  <img src="https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python&logoColor=white&color=3776AB" alt="Python" />
  <img src="https://img.shields.io/badge/-Google_Gemini-black?style=for-the-badge&logo=google&logoColor=white&color=4285F4" alt="Google Gemini" />
  <img src="https://img.shields.io/badge/-Vertex_AI-black?style=for-the-badge&logo=googlecloud&logoColor=white&color=4285F4" alt="Vertex AI" />
  <img src="https://img.shields.io/badge/-Langchain-black?style=for-the-badge&logo=python&logoColor=white&color=F4A261" alt="Langchain" />
  <img src="https://img.shields.io/badge/-Streamlit-black?style=for-the-badge&logo=streamlit&logoColor=white&color=FF4B4B" alt="Streamlit" />
  </div>


</div>

## 📋 <a name="table">Table of Contents</a>

1. 🤖 [Introduction](#introduction)
2. ⚙️ [Tech Stack](#tech-stack)
3. 🔋 [Features](#features)
4. 🤸 [Quick Start](#quick-start)


## <a name="introduction">🤖 Introduction</a>

This project implements a Quiz Builder using various technologies such as Google Gemini, Vertex AI API, embeddings, Google Service Account, Langchain, PDF loader, and Streamlit. 


## <a name="tech-stack">⚙️ Tech Stack</a>

- **Python**: The primary programming language used for developing the backend logic and integrating various APIs and services.
- **Google Gemini**: Utilized for advanced document processing, enabling efficient analysis and extraction of key information.
- **Vertex AI API**: Integrated for generating quizzes and other AI-driven functionalities, providing robust machine learning capabilities.
- **Langchain**: Employed for creating text embeddings, enhancing the model's understanding and representation of textual data.
- **Streamlit**: Implemented for building an interactive and user-friendly interface, allowing users to easily generate and interact with quizzes.

## <a name="features">🔋 Features</a>

👉 **Document Processing**: Processes input documents to extract and analyze relevant information, setting the foundation for quiz generation.

👉 **Quiz Generation**: Automatically creates quizzes based on user-provided documents and topics, leveraging AI models to ensure relevance and accuracy.

👉 **Text Embeddings**: Utilizes advanced techniques to generate text embeddings, enhancing the understanding of document content and quiz questions.

👉 **Secure Authentication**: Integrates Google Service Account for secure and efficient access to necessary APIs and services.

👉 **Interactive User Interface**: Offers a user-friendly interface through Streamlit, making it easy for users to input data, generate quizzes, and interact with the application.

👉 **PDF Ingestion**: Supports the ingestion and processing of PDF documents, allowing users to upload and work with various formats.

👉 **Answer Explanations**: Provides detailed explanations for quiz answers, helping users understand the reasoning behind each response.

👉 **Navigation Controls**: Includes intuitive navigation controls for a smooth quiz-taking experience, allowing users to easily move through questions.

👉 **rror Handling and Validation**: Ensures robust error handling and input validation, improving the application's reliability and user experience.

👉 **Packaging and Deployment**: Considers packaging and deployment best practices, ensuring the application is easy to distribute and set up.



## <a name="quick-start">🤸 Quick Start Installation</a>

Follow these steps to set up the project locally on your machine.

**Prerequisites**

Make sure you have the following installed on your machine:

**Python**: Required for running the backend logic and integrating various APIs. - https://www.python.org/downloads/
**Git**: Essential for version control and managing the project's codebase - https://git-scm.com/
**Google Cloud SDK**: Necessary for accessing Google APIs and managing Google Service Account credentials.
**Streamlit**: Needed for creating and running the interactive user interface. - https://streamlit.io/

**Cloning the Repository**

```bash
git clone https://github.com/RayMoham/Mission-Quizify--MyVersion.git
```

**Installation**

Install the necessary dependencies listed in `requirements.txt`.



**Set Up Environment Variables**
- Variables are setup but create own Google Cloud SDK console


```bash
 embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "Project_ID",
        "location": "us-central1"
        
```


**Running the Project**

Run the Streamlit application by executing `streamlit run xxx.py` in the terminal where xxx is the name of the py file you want to run.

```bash
streamlit run task_10.py
```

It will open in your browser to view the project.
