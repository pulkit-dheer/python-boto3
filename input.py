import os


folders = input("Please provde list of folders list of folders manes with spaces in between: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a vaild folder name")
        break
    except PermissionError:
        print("No access to folder: " + folder)
        break
    for file in files:
        print(file)