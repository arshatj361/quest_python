import os
import shutil

print(os.getcwd())

os.mkdir("Folder1")
file = open("Folder1/blank2.txt",'x')
file.close()
os.mkdir("Folder2")

shutil.copyfile("Folder1/blank2.txt","Folder2/blank.txt")
