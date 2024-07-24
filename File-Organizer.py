import os
import shutil

def organize_files(directory):
    categories = {
        "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff"],
        "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".mkv"],
        "Music": [".mp3", ".wav", ".ogg", ".flac"],
        "Documents": [".doc", ".docx", ".txt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Programs": [".exe", ".msi"],
        "Scripts": [".py", ".sh", ".bat"],
        "Spreadsheets": [".csv"],
        "Presentations": [".ppt", ".pptx"],
        "Web Pages": [".html", ".htm"],
        "Others": []
    }

    for category in categories:
        os.makedirs(os.path.join(directory, category), exist_ok=True)

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_extension = os.path.splitext(filename)[1].lower()

            category_found = False
            for category, extensions in categories.items():
                if file_extension in extensions:
                    shutil.move(filepath, os.path.join(directory, category, filename))
                    category_found = True
                    break

            if not category_found:
                shutil.move(filepath, os.path.join(directory, "Others", filename))

    print("File organization completed.")

def main():
    print("Welcome to File Organizer!")
    directory = input("Enter the directory path to organize files: ").strip()

    while not os.path.isdir(directory):
        print("Directory does not exist.")
        directory = input("Enter a valid directory path: ").strip()

    organize_files(directory)
    print("Files organized successfully.")

if __name__ == '__main__':
    main()