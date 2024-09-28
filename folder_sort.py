import os
import shutil
import re

def organize_and_rename_files(source_directory):
    # Get a list of all files in the specified directory
    files = os.listdir(source_directory)

    for file in files:
        # Check if the element is a file
        if os.path.isfile(os.path.join(source_directory, file)):
            # Search for text in parentheses
            match = re.search(r'\((.*?)\)', file)
            if match:
                new_name = match.group(1) + '.ogg'  # Extract text inside parentheses and add .ogg
                folder_name = file.split('#')[0].strip()  # Remove spaces for folder name

                # Create the path to the new folder
                new_folder_path = os.path.join(source_directory, folder_name)

                # Create the folder if it doesn't exist
                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)

                # Path to the old file
                old_file_path = os.path.join(source_directory, file)

                # Path to the new file
                new_file_path = os.path.join(new_folder_path, new_name)

                # Rename and move the file to the new folder
                shutil.move(old_file_path, new_file_path)

# Specify the directory where your files are located
source_directory = 'C:\\Path\\To\\YourFiles'

organize_and_rename_files(source_directory)
