import tkinter as tk
from tkinter import filedialog
import os
import shutil

def choose_directory():
    directory_path = filedialog.askdirectory(title="Choose a Directory")

    files = os.listdir(directory_path)
    list = []
    for file in files:
        list.append(file)

    for file_name in list:
        if(not os.path.exists(file_name.split(".")[1])):
            os.mkdir(file_name.split(".")[1])
        shutil.move(f'{directory_path}/{file_name}', file_name.split(".")[1])
   
root = tk.Tk()
# Create a button to trigger the directory dialog
directory_button = tk.Button(root, text="Choose Directory", command=choose_directory)
directory_button.pack(pady=75)

root.mainloop()