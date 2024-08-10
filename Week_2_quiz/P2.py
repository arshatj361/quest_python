import os
import shutil

print(os.getcwd())

try:

    os.mkdir("Folder1")
    file = open("Folder1/blank2.txt",'x')
    file.close()
    os.mkdir("Folder2")
    shutil.copyfile("Folder1/blank2.txt","Folder2/blank.txt") 

except Exception as e:
    print(f"no file found in the source":{e})

except Exception as e:
    print(f"file with same name already exists":{e})
except Exception as e:
    print(f"An error occured:{e}")
      

