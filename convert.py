import os
import re

def replace_layout_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace 'layout: default' with 'layout: page'
    new_content = re.sub(r'layout:\s*default', 'layout: page', content)

    # Only write back if a change was made
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        return True
    return False

def find_and_replace_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if replace_layout_in_file(file_path):
                    print(f"Updated layout in: {file_path}")

# Replace 'your_directory_path' with the path to the directory you want to search
find_and_replace_in_directory('./')
