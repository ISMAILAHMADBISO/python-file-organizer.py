import os
import shutil

# Dictionary to map file extensions to folder names
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.txt', '.pdf', '.docx', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.tar', '.gz'],
}

def create_folders(base_dir):
    """
    Creates folders for each category if they don't exist.
    """
    for category in file_categories:
        folder_path = os.path.join(base_dir, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")

def move_file(file_path, category_folder):
    """
    Moves a file to the respective category folder.
    """
    try:
        shutil.move(file_path, category_folder)
        print(f"Moved {file_path} to {category_folder}")
    except Exception as e:
        print(f"Error moving file {file_path}: {e}")

def organize_files(base_dir):
    """
    Organizes files in the specified directory into categories.
    """
    create_folders(base_dir)
    
    # Loop through all files in the base directory
    for file_name in os.listdir(base_dir):
        file_path = os.path.join(base_dir, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get file extension
        _, file_extension = os.path.splitext(file_name)
        
        # Check if the file extension matches any category
        moved = False
        for category, extensions in file_categories.items():
            if file_extension.lower() in extensions:
                category_folder = os.path.join(base_dir, category)
                move_file(file_path, category_folder)
                moved = True
                break
        
        # If the file didn't match any category, move it to a general 'Others' folder
        if not moved:
            others_folder = os.path.join(base_dir, 'Others')
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            move_file(file_path, others_folder)

def main():
    """
    Main function to drive the automation.
    """
    base_dir = input("Enter the directory path to organize files: ")
    
    if not os.path.isdir(base_dir):
        print("The specified path is not a valid directory.")
        return
    
    print("Starting file organization...")
    organize_files(base_dir)
    print("File organization complete.")

if __name__ == "__main__":
    main()
