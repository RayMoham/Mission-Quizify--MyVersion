import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from tasks.task_3.task_3 import DocumentProcessor
from tasks.task_4.task_4 import EmbeddingClient
from tasks.task_5.task_5 import ChromaCollectionCreator


if __name__ == "__main__":
    st.header("Quizzify")

    # Configuration for EmbeddingClient
    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "axiomatic-area-423218-h7",
        "location": "us-central1"
    }
    
    screen = st.empty() # Screen 1, ingest documents
    with screen.container():
       

        processor = DocumentProcessor()
        processor.ingest_documents()
        
        embedding_client = EmbeddingClient(embed_config["model_name"], embed_config["project"], embed_config["location"])
        
        chroma_creator = ChromaCollectionCreator(processor, embedding_client)

    with st.form("Load Data to Chroma"):
        st.subheader("Quiz Builder")
        st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
            
        quiz_topic = st.text_input("Enter Quiz Topic")
        num_questions = st.slider("Select Number of Questions", 1, 10)
            
        document = None
            
        submitted = st.form_submit_button("Generate a Quiz!")
        if submitted:
                
            chroma_collection = chroma_creator.create_chroma_collection()     
                
            document = chroma_creator.query_chroma_collection(quiz_topic) 
                
    if document:
        screen.empty() # Screen 2
        with st.container():
            st.header("Query Chroma for Topic, top Document: ")
            st.write(document)
