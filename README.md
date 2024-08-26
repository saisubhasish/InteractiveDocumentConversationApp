# Interactive Document Chat

This application allows users to upload PDF or Word documents and chat with the content using advanced language models.

![Screenshot 2024-08-26 163455](https://github.com/user-attachments/assets/7a1b3542-3f3a-430f-aeec-407e45351d92)


## Features

- Upload PDF and Word documents
- Process and index document content
- Chat interface for asking questions about the documents
- Integration with Groq LLM and FAISS vector store

## Installation

1. Clone this repository
   ```
   https://github.com/saisubhasish/InteractiveDocumentConversationApp.git
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add your Groq API key: `GROQ_API_KEY=your_api_key_here`

## Usage

Run the Streamlit app:

```
streamlit run app/main.py
```

Then, follow the on-screen instructions to upload a document and start chatting.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
"""

gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class

# Virtual Environment
venv/
env/

# IDEs
.vscode/
.idea/

# Streamlit
.streamlit/

# Environment variables
.env

# OS generated files
.DS_Store
Thumbs.db

# Project specific
*.pdf
*.docx
*.doc
