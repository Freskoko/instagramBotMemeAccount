import os

subreddit = "okbuddyretard"
zipName = f"{subreddit}_hot.zip"

directory = (fr"C:\Users\Henrik\Downloads\{zipName}")
directory = r"C:\Users\Henrik\Downloads\okbuddyretard_hot.zip"

import os
import zipfile
files = zipfile.ZipFile(directory, "r")
for name in files.namelist():
    data = files.read(name)
    pathName = os.path.abspath(fr"C:\Users\Henrik\Downloads\okbuddyretard_hot\{name}.jpg")
    coolPath = os.path.join(directory, name)
    print(pathName)
    print(coolPath)