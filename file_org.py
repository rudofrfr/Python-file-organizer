import os
import shutil

dictionary = {
    ".doc":"Word files",
    ".docx":"Word files",
    ".pdf":"PDF files",
    ".txt":"Text files",
    ".jpg":"Photos",
    ".webp":"Photos",
    ".JPEG":"Photos",
    ".png":"Photos",
    ".mp3":"Audio files",
    ".wav":"Audio files",
    ".mp4":"Video files",

}


folder = input("Insert the path to the directory/folder  ")
os.chdir(folder)


files = os.listdir()
for file in files:

    splitters = os.path.splitext(file)
    ext_getter = dictionary.get(splitters[1])

    if ext_getter == "Word files":
        target_folder = os.path.join(folder, "Word files")
        if os.path.exists(target_folder):
            shutil.move(file, target_folder)
        else:
            os.mkdir(target_folder)
            shutil.move(file, target_folder)

    elif ext_getter == "PDF files":
        target_folder = os.path.join(folder, "PDF files")
        if os.path.exists(target_folder):
            shutil.move(file, target_folder)
        else:
            os.mkdir(target_folder)
            shutil.move(file, target_folder)

    elif ext_getter == "Text files":
        target_folder = os.path.join(folder, "Text files")
        if os.path.exists(target_folder):
            shutil.move(file, target_folder)
        else:
            os.mkdir(target_folder)
            shutil.move(file, target_folder)
    
    elif ext_getter == "Photos":
        target_folder = os.path.join(folder, "Photos")
        if os.path.exists(target_folder):
            shutil.move(file, target_folder)
        else:
            os.mkdir(target_folder)
            shutil.move(file, target_folder)

    elif ext_getter == "Audio files":
        target_folder = os.path.join(folder, "Audio files")
        if os.path.exists(target_folder):
            shutil.move(file, target_folder)
        else:
            os.mkdir(target_folder)
            shutil.move(file, target_folder)

    elif ext_getter == "Video files":
        target_folder = os.path.join(folder, "Video files")
        if os.path.exists(target_folder):
            shutil.move(file, target_folder)
        else:
            os.mkdir(target_folder)
            shutil.move(file, target_folder)






