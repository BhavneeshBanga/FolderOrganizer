import tkinter as tk
from tkinter import filedialog
import os
import shutil

def choose_directory():
    directory_path = filedialog.askdirectory(title="Choose a Directory")

    list = os.listdir(directory_path)

    for file_name in list:
        folder_name = (file_name.split(".")[1])
        if(not os.path.exists(directory_path + '/' + str(folder_name))):
            destination_path = directory_path + '/' + str(folder_name)
            os.mkdir(destination_path)
        shutil.move(f'{directory_path}/{file_name}', destination_path)
   
root = tk.Tk()
# Create a button to trigger the directory dialog
directory_button = tk.Button(root, text="Choose Directory", command=choose_directory)
directory_button.pack(pady=75)

root.mainloop()