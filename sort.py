import sys

def main():
    try:
        path = sys.argv[1]
    except IndexError:
        print("Error. Path to the folder is required")
        return
    
    print(path)

main()