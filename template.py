import os
from pathlib import Path  
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s: %(levelname)s: %(message)s]'
)

while True:
    project_name = input("Enter the project name: ")
    if project_name != '':
        break

logging.info(f'Creating project by name: {project_name}')

#list of files:

list_of_files = [
    f"src/{project_name}/__init__.py",   
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(Path(file_path))
    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"creating a directory at: {file_dir} for file: {file_name}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0 ):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating a new file: {file_name} at path: {file_path}")
    else:
        logging.info(f"File is already is present at: {file_path}")