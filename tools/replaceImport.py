import os
import re

def replace_imports_in_file(file_path, old_module, new_module):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace import statements
    new_content = content
    new_content = re.sub(rf'\bimport {old_module}\b', f'import {new_module}', new_content)
    new_content = re.sub(rf'\bfrom {old_module} import\b', f'from {new_module} import', new_content)
    new_content = re.sub(rf'\b{old_module}\.', f'{new_module}.', new_content)

    # Replace all module usage
    new_content = re.sub(rf'\b{old_module}\b', new_module, new_content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Replaced in file: {file_path}")
    else:
        print(f"No changes in file: {file_path}")

def replace_imports_in_directory(directory, old_module, new_module):
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                replace_imports_in_file(file_path, old_module, new_module)

if __name__ == "__main__":
    # 指定要替换的目录
    directory_path = "../code/"

    # 指定要替换的库名
    old_module_name = "urequests"
    new_module_name = "SeniorOS.lib.mrequests"

    replace_imports_in_directory(directory_path, old_module_name, new_module_name)
