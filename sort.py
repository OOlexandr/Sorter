import sys
import os

file_types = {
    "images": [".jpeg", ".jpg", ".png", ".svg"],
    "video": [".avi", ".mp4", ".mov", ".mkv"],
    "documents": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"],
    "audio": [".mp3", ".ogg", ".wav", ".amr"],
    "archives": [".zip", ".gz", ".tar"]}

def prepare(directory):
    #Checks if folders for all the types of file exists
    #and creates them if they do not exist
    for type in file_types:
        path = os.path.join(directory, type)
        if not os.path.exists(path):
            os.makedirs(path)

def log(sort_result):
    #sort_result - dict, that holds information about sorted files,
    #met extensions and unknown extensions
    #inputs this information in files "catalogue.txt" in folders corresponding to each type
    #and in files "found_extensions.txt" and "unknown_extensions.txt" in the root of the folder

    #TODO
    print(sort_result)

def iterate(root, relative_path = "", search_data = {}):
    #walks through the folder sorts files and records data about them
    #returns dictionary, storing all the recorded data

    if not search_data:
    #initializing the search data
        for type in file_types:
            search_data[type] = []
        search_data["unknown"] = []
        #a key for every file type, including those of unknown types
        search_data["found_extensions"] = set()
        search_data["unknown_extensions"] = set()
        #a key for found known extensions and unknown extensions

    dir_path = os.path.join(root, relative_path)
    for entry in os.listdir(dir_path):
        relative_entry_path = os.path.join(relative_path, entry)
        entry_path = os.path.join(dir_path, entry)
        if os.path.isdir(entry_path):
            search_data = iterate(root, relative_path=relative_entry_path, search_data=search_data)
        else:
            extension = os.path.splitext(entry_path)[1]

            is_type_recognized = False
            for type in file_types:
                if extension in file_types[type]:
                    search_data[type].append(entry_path)
                    search_data["found_extensions"].add(extension)
                    is_type_recognized = True
                    break
            if not is_type_recognized:
                search_data["unknown"].append(entry_path)
                search_data["unknown_extensions"].add(extension)
    
    return search_data

def sort(path):
    prepare(path)
    log(iterate(path))

def main():
    try:
        #path = sys.argv[1]
        path = "D:\\TestFolder" #for debugging
        sort(path)
    except IndexError:
        print("Error. Path to the folder is required")
        return
    except FileNotFoundError:
        print("Error. Specified path is not valid")
        return

main()