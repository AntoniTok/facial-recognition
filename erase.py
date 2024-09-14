import os
import shutil

def clear_folder(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return None

    # Iterate over and delete the files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")
