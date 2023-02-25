import sys
import os

def iterate(path):
    for entry in os.listdir(path):
        print(entry)


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