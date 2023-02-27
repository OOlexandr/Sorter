import sys
import os

def iterate(root, path = []):
    dir_path = root
    for dir in path:
        dir_path = os.path.join(dir_path, dir)
    for entry in os.listdir(dir_path):
        entry_path = os.path.join(dir_path, entry)
        if os.path.isdir(entry_path):
            iterate(root, path = path+[entry])
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