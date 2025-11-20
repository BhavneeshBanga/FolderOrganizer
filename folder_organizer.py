import os
import shutil

files = os.listdir('garbage/')
list = []
for file in files:
    list.append(file)

for file_name in list:
    if(not os.path.exists(file_name.split(".")[1])):
        os.mkdir(file_name.split(".")[1])
    shutil.move(f'garbage/{file_name}', file_name.split(".")[1])
