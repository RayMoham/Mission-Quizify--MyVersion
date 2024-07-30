import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import os
import tempfile
import uuid
class DocumentProcessor:

    def __init__(self):
        self.documents = []
        self.pages = []


    def ingest_documents(self):

        uploaded_files = st.file_uploader("Upload PDF files", type='pdf', accept_multiple_files=True)
        if uploaded_files:

            for uploaded_file in uploaded_files:
                unique_id = uuid.uuid4().hex
                original_name, file_extension = os.path.splitext(uploaded_file.name)

                temp_file_name = f"{original_name}_{unique_id}{file_extension}"
                temp_file_path = os.path.join(tempfile.gettempdir(), temp_file_name)

                with open(temp_file_path, 'wb') as f:
                    f.write(uploaded_file.getbuffer())
                pdf_loader = PyPDFLoader(file_path=temp_file_path)
                document_list = pdf_loader.load()
                self.documents.extend(document_list)
                os.unlink(temp_file_path)

            # Display the total number of documents processed
            st.write(f"Total documents processed: {len(self.documents)}")

if __name__ == "__main__":
    
    st.title("PDF Document Processor")
    processor = DocumentProcessor()
    processor.ingest_documents()
