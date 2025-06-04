import os
from pathlib import Path


def search(name):


    home = Path.home()

    downloads = home / 'Downloads'
    documents = home / "Documents"

    target_dirs = [downloads, documents]

    for directory in target_dirs:
        if directory.exists():
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.split(".")[0].lower().find(name) != -1:
                        exit()
                        print(file.split(".")[0])
                        
        else:
            print("Did not work")


def main():
    exit()

#This should be the code that finds the name of the file that the user wants to search
