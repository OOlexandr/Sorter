import sys
import os
import shutil

file_types = {
    "images": [".jpeg", ".jpg", ".png", ".svg"],
    "video": [".avi", ".mp4", ".mov", ".mkv"],
    "documents": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"],
    "audio": [".mp3", ".ogg", ".wav", ".amr"],
    "archives": [".zip", ".gz", ".tar"]}

def move_audio(root, files):
    destination = os.path.join(root, "audio")
    if not os.path.exists(destination):
        os.makedirs(destination)
    for file in files:
        file_path = os.path.join(root, file)
        new_file_name = os.path.basename(file) #later names will be normalized here
        new_file_path = os.path.join(destination, new_file_name)
        os.rename(file_path, new_file_path)
def move_video(root, files):
    destination = os.path.join(root, "video")
    if not os.path.exists(destination):
        os.makedirs(destination)
    for file in files:
        file_path = os.path.join(root, file)
        new_file_name = os.path.basename(file) #later names will be normalized here
        new_file_path = os.path.join(destination, new_file_name)
        os.rename(file_path, new_file_path)
def move_images(root, files):
    destination = os.path.join(root, "images")
    if not os.path.exists(destination):
        os.makedirs(destination)
    for file in files:
        file_path = os.path.join(root, file)
        new_file_name = os.path.basename(file) #later names will be normalized here
        new_file_path = os.path.join(destination, new_file_name)
        os.rename(file_path, new_file_path)
def move_documents(root, files):
    destination = os.path.join(root, "documents")
    if not os.path.exists(destination):
        os.makedirs(destination)
    for file in files:
        file_path = os.path.join(root, file)
        new_file_name = os.path.basename(file) #later names will be normalized here
        new_file_path = os.path.join(destination, new_file_name)
        os.rename(file_path, new_file_path)
def move_archives(root, files):
    destination = os.path.join(root, "archives")
    if not os.path.exists(destination):
        os.makedirs(destination)
    for archive in files:
        archive_path = os.path.join(root, archive)
        new_archive_name = os.path.splitext(os.path.basename(archive))[0]
        #later names will be normalized here
        new_archive_path = os.path.join(destination, new_archive_name)
        shutil.unpack_archive(archive_path, new_archive_path)
        os.remove(archive_path)
#"add functions, responsible for work with every file type" - task.

moving_functions = {
    "images": move_images,
    "video": move_video,
    "documents": move_documents,
    "audio": move_audio,
    "archives": move_archives
}

def move_files(root, catalogue):
    for type in file_types:
        if catalogue[type]:
            moving_functions[type](root, catalogue[type])


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
    #outputs this information into console

    #TODO
    print(sort_result)

def catalogue(root, relative_path = "", search_data = {}, ignore = []):
    #walks through the folder sorts files and records data about them
    #returns dictionary, with the recorded data

    if not search_data:
    #initializing the search data
        for type in file_types:
            search_data[type] = []
        #a key for every file type
        search_data["found_extensions"] = set()
        search_data["unknown_extensions"] = set()
        #a key for found known extensions and unknown extensions

    dir_path = os.path.join(root, relative_path)
    for entry in os.listdir(dir_path):
        if entry in ignore:
            continue
        relative_entry_path = os.path.join(relative_path, entry)
        entry_path = os.path.join(dir_path, entry)
        if os.path.isdir(entry_path):
            search_data = catalogue(root, relative_path=relative_entry_path, search_data=search_data)
        else:
            extension = os.path.splitext(entry_path)[1]

            is_type_recognized = False
            for type in file_types:
                if extension in file_types[type]:
                    search_data[type].append(relative_entry_path)
                    search_data["found_extensions"].add(extension)
                    is_type_recognized = True
                    break
            if not is_type_recognized:
                search_data["unknown_extensions"].add(extension)
    
    return search_data

def sort(path):
    #prepare(path) obsolete
    files = catalogue(path, ignore = file_types.keys())
    log(files)
    move_files(path, files)

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