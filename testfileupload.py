import os
import time

directory = r"C:\Users\Henrik\Documents\PROGRAMMING\Instagram bot\memesToUpload"

for filename in os.scandir(directory):
    if filename.is_file():
        time.sleep(1)
        print(filename.path)