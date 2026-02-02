# codebase-merger-by-Wahaz-Softs-github.com/Wahaze
A Python script to merge your project's entire code base into a single text file: you will get all the codes from all files in one. It recursively scans directories, intelligently ignoring dependencies (e.g., node_modules) and build artifacts. Ideal for creating a complete snapshot for archiving or feeding your project's code to an AI for analysis.

# Project Consolidator

A simple and effective Python script to consolidate all text files in a project into a single output file. Ideal for archiving, code sharing, or providing full context to Large Language Models (LLMs).

## 🚀 Why Use This Script?

When working with Large Language Models (like GPT-4, Claude, etc.), it's often necessary to provide them with the entire context of a project to get accurate answers. Manually copying and pasting each file is tedious and error-prone.

This script automates the process by:
- Recursively scanning your project directory.
- Ignoring unnecessary folders and files (`node_modules`, `dist`, `package-lock.json`...).
- Detecting and reading only text-based files.
- Automatically handling different file encodings (UTF-8, etc.).
- Creating a single, clean, and well-formatted `.txt` file with all your code.

## ✨ Features

-   **Recursive Traversal**: Scans the provided directory and all its subdirectories.
-   **Intelligent Filtering**: By default, excludes `node_modules`, `dist`, `dist-electron` folders and the `package-lock.json` file.
-   **Text File Detection**: Uses `chardet` to distinguish text files from binaries (images, executables, etc.).
-   **Encoding Management**: Correctly detects and decodes files, preventing corrupted character issues.
-   **Formatted Output**: The final file is well-structured, with a header for each file indicating its original name and path.

## 🛠️ Prerequisites

-   Python 3.x
-   The `chardet` library.

You can install the required library using pip:
```bash
pip install chardet```

## ⚙️ Usage

1.  Save the script as `consolidate.py` (or any other name you prefer).

2.  Open a terminal or command prompt.

3.  Run the script, passing the path to your project directory as an argument.

    ```bash
    python consolidate.py /path/to/your/project
    ```

    **Example on Windows:**
    ```bash
    python consolidate.py C:\Users\YourName\Documents\MyAwesomeProject
    ```

    **Example on macOS/Linux:**
    ```bash
    python consolidate.py ~/projects/my-awesome-project
    ```

4.  The script will create a file named `contenu_<project_name>.txt` in the directory where you ran the command. This file will contain the entire codebase of your project.

## 🔧 Customization

You can easily adapt the script to your needs by modifying the `doit_ignorer_chemin` (or `should_ignore_path`) function.

For example, to also ignore `.env` files and the `build` directory:

```python
def should_ignore_path(path):
    # List of excluded folders
    excluded_folders = ['node_modules', 'dist', 'dist-electron', 'build'] # <--- Add 'build' here
    
    # Check if the path contains any of the excluded folders
    for folder in excluded_folders:
        if f'/{folder}/' in path.replace('\\', '/') or path.replace('\\', '/').endswith(f'/{folder}'):
            return True
    
    # Check if it is an excluded file
    excluded_files = ['package-lock.json', '.env'] # <--- Add '.env' here
    if os.path.basename(path) in excluded_files:
        return True
        
    return False
```
*Note: Remember to also rename the function call inside `parcourir_repertoire` (or `traverse_directory`) if you rename the function itself.*

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
