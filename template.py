import os
import yaml

def create_directory_structure():
    directories = [
        "app",
        "tests",
        "config",
        "src"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        
    print("Directory structure created successfully.")

def create_files():
    files = {
        "app/__init__.py": "",
        "app/main.py": "# main_py_content",
        "app/document_processor.py": "# document_processor_py_content",
        "app/vector_store.py": "# vector_store_py_content",
        "app/llm_interface.py": "# llm_interface_py_content",
        "app/chat_interface.py": "# chat_interface_py_content",
        "tests/__init__.py": "",
        "tests/test_document_processor.py": "# test_document_processor_py_content",
        "tests/test_vector_store.py": "# test_vector_store_py_content",
        "tests/test_llm_interface.py": "# test_llm_interface_py_content",
        "tests/test_chat_interface.py": "# test_chat_interface_py_content",
        "config/config.yaml": "# config_yaml_content",
        "requirements.txt": "# requirements_txt_content",
        "README.md": "# readme_md_content",
        ".gitignore": "# gitignore_content",
        "src/logger.py": "# logger_py_content",
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

