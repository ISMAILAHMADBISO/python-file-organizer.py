# Python File Organizer

A Python based file management and automation tool that automatically organizes files into categorized folders based on their file extensions. It uses Python's built-in `os` and `shutil` modules to simplify file organization and reduce manual work.

## Features

- Automatically categorizes files by extension.
- Creates folders for Images, Documents, Videos, Audio, and Archives.
- Moves unrecognized file types into an Others folder.
- Checks whether the selected directory exists before organizing.
- Handles file movement errors.
- Uses Python's built-in libraries, requiring no external dependencies.

## Project Structure

```text
python-file-organizer/
├── file_organizer.py
└── README.md
```

## Technologies Used

- Python 3
- os module
- shutil module

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ISMAILAHMADBISO/python-file-organizer.git
```

### 2. Navigate to the project directory

```bash
cd python-file-organizer
```

### 3. Run the program

```bash
python file_organizer.py
```

### 4. Enter the directory path

When prompted, enter the path of the folder you want to organize.

Example:

```text
Enter the directory path to organize files: C:\Users\YourName\Downloads
```

The program will create the necessary category folders and move files into them.

## Supported File Types

| Category | Extensions |
|---|---|
| Images | .jpg, .jpeg, .png, .gif, .bmp |
| Documents | .txt, .pdf, .docx, .xlsx, .pptx |
| Videos | .mp4, .mkv, .avi, .mov, .flv |
| Audio | .mp3, .wav, .aac |
| Archives | .zip, .tar, .gz |
| Others | All unsupported file extensions |

## Requirements

- Python 3.x
- No external packages required.

## Important Note

Test the program on a sample folder before using it on important files. The script moves files from their original locations, so make sure you have backups where necessary.

## Future Improvements

- Preview mode before moving files.
- Duplicate filename detection and handling.
- Activity logging.
- Support for custom file categories.
- Recursive folder organization.
- Graphical user interface (GUI).

## Author

Ismail Ahmad

GitHub: [ISMAILAHMADBISO](https://github.com/ISMAILAHMADBISO)

## License

This project is open-source and available under the MIT License. Add a LICENSE file to the repository if you choose to distribute it under that license.
