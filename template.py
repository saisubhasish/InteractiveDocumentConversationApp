import os
import yaml

def create_directory_structure():
    directories = [
        "config",
        "utils",
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        
    print("Directory structure created successfully.")

def create_files():
    files = {
        "utils/__init__.py": "",
        "utils/document_processor.py": "# document_processor_py_content",
        "utils/vector_store.py": "# vector_store_py_content",
        "utils/llm_interface.py": "# llm_interface_py_content",
        "utils/chat_interface.py": "# chat_interface_py_content",
        "utils/logger.py": "# logger_py_content",
        "utils/exception.py": "# exception_py_content",
        "config/config.yaml": "# config_yaml_content",
        "app.py": "# app_py_content",
        "setup.py": "# setup_py_content",
        "requirements.txt": "# requirements_txt_content",
        "README.md": "# readme_md_content",
        ".gitignore": "# gitignore_content",
        ".env": "# .env_content"
    }
    
    for file_path, content in files.items():
        with open(file_path, "w") as f:
            f.write(content)
        print(f"Created {file_path}")

if __name__ == "__main__":
    create_directory_structure()
    create_files()
    print("Project structure  created successfully.")

