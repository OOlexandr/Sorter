import sys
import os

def iterate(root, relative_path = ""):
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