import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import os
import shutil

class BrowseFunc():
    def __init__(self, root, text, col, row, btn_name, folder='./Faces'):
        self.root = root
        self.text = text
        self.col = col
        self.row = row
        self.btn_name = btn_name
        self.target_dir = f'{folder}/{self.btn_name[:-13]}'

    def arange(self, face_path, col, row):
        face_logo = Image.open(f'{face_path}')
        face_logo = ImageTk.PhotoImage(face_logo)
        face_label = tk.Label(image=face_logo)
        face_label.image = face_logo
        face_label.grid(column=col, row=row)

    def copy_move_file(self):
        shutil.rmtree(self.target_dir)
        os.mkdir(self.target_dir)

        shutil.copy(f'{self.file.name}', self.target_dir)

    def exe(self):
        self.text.set('Loading...')

        self.file = askopenfile(parent=self.root, mode='rb', title='Choose a file', filetypes=[('PNG Image', '*.png'), ('JPEG Image', '*jpg'), ('GIF Image', '*.gif')])
        self.arange(self.file.name, self.col, self.row)
        self.copy_move_file()
        
        self.text.set(self.btn_name[:-13])