import sys
import os

file_types = ("images", "video", "documents", "audio", "archives")

def prepare(directory):
    #Checks if folders for all the types of file exists
    #and creates them if they do not exist
    for type in file_types:
        path = os.path.join(directory, type)
        if not os.path.exists(path):
            os.makedirs(path)

def iterate(root, relative_path = ""):
    if not relative_path:
        prepare(root)
    #will execute only once in the beginning of iteration
    
    dir_path = os.path.join(root, relative_path)
    for entry in os.listdir(dir_path):
        relative_entry_path = os.path.join(relative_path, entry)
        entry_path = os.path.join(dir_path, entry)
        if os.path.isdir(entry_path):
            iterate(root, relative_path = relative_entry_path)
        else:
            print(entry_path)


def main():
    try:
        path = sys.argv[1]
        iterate(path)
    except IndexError:
        print("Error. Path to the folder is required")
        return
    except FileNotFoundError:
        print("Error. Specified path is not valid")
        return

main()