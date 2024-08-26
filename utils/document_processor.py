import os
import tempfile
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def process_document(uploaded_file):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        # Write the contents of the uploaded file to the temporary file
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    try:
        # Determine file type and use appropriate loader
        file_extension = os.path.splitext(uploaded_file.name)[1].lower()
        if file_extension == ".pdf":
            loader = PyPDFLoader(tmp_file_path)
        elif file_extension in [".docx", ".doc"]:
            loader = Docx2txtLoader(tmp_file_path)
        else:
            raise ValueError("Unsupported file type")
        
        documents = loader.load()
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
        
        return texts
    finally:
        # Clean up the temporary file
        os.unlink(tmp_file_path)