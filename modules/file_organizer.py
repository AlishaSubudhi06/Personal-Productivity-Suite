import os

def organize_files():
    path = input("Enter folder path: ")

    if not os.path.exists(path):
        print("Folder not found")
        return

    files = os.listdir(path)

    print("Files in folder:")
    for file in files:
        print(file)