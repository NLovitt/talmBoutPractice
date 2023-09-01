import os
import shutil

#path to folder to be organized
path = input("Enter the path of the folder to be organized: ")

#list of all files in the folder
list_ = os.listdir(path)


# create a dictionary to store the extension types the key their folder names
dict_ = {
    '_audio' : ('mp3', 'm4a', 'wav', 'flac'),
    '_video' : ('mp4', 'mkv', 'MKV', 'flv', 'mpeg', 'webm'),
    '_documents' : ('doc', 'pdf', 'txt'),
    '_images' : ('jpg', 'png', 'jpeg'),
    '_webp' : ('webp')
}

# create a function to find the extension of the file
def file_finder(file_name):
    #differentiate between files and folders
    if os.path.isfile(os.path.join(path, file_name)) is False:
        return None
    # find the extension of the file
    extension = file_name.split(".")[-1]
    
    # for extension_type in dict_:
    #     if extension in dict_[extension_type]:
    #         return extension_type

    #re-write for loop above using .items()
    for extension_type, extension_tuple in dict_.items():
        if extension in extension_tuple:
            return extension_type


    return '_misc'


# create a function to move the files to the folders
def move_file(file_name):
    # find the extension type
    if file_finder(file_name) is not None:
        file_extension = file_finder(file_name)
        # find the path of the extension type
        path_ = os.path.join(path, file_extension)

        # if the path does not exist, create a new folder
        if os.path.exists(path_) is False:
            os.mkdir(path_)
        # move the file to the new folder
        shutil.move(os.path.join(path, file_name), os.path.join(path_, file_name))

# run the function for every file in the folder
for file_ in list_:
    move_file(file_)
print('Done!')
