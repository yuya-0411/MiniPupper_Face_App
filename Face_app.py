import tkinter as tk
from PIL import Image, ImageTk
from functions import BrowseFunc
from face_setup import SETUP
import os
import shutil

class APP():
    def __init__(self):
        self.setup = SETUP()
        self.face_store = self.setup.folder()
        self.root = tk.Tk()
        self.root.title('MiniPupper Face App')
        self.generate_canvas(width=1020, height=720, columnspan=3, rowspan=4)
        self.generate_menu()
        self.initial_img()
        self.generate_buttons()
    
    def generate_canvas(self, width, height, columnspan, rowspan):
        # Canvas
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.grid(columnspan=columnspan, rowspan=rowspan)

    def generate_menu(self):
        #create menu
        menu = tk.Menu(self.root)

        #set the menu on the window
        self.root.config(menu=menu)

        #create parent menu on the menu 
        menu_file = tk.Menu(self.root) 
        menu.add_cascade(label='MENU', menu=menu_file)

        # child menu on the parent menu
        menu_file.add_command(label='Reset', command=lambda:self.initial_img()) 
        menu_file.add_separator() 
        menu_file.add_command(label='UpDate', command=lambda:self.setup.face_setup()) 
        menu_file.add_separator() 
        menu_file.add_command(label='close app', command=lambda:self.root.destroy())

    def initial_img(self):
        # initial images
        self.Faces = [
                    'logo/original.png',
                    'notconnect/original.png',
                    'sleep/original.gif',
                    'turnaround/original.png',
                    'walk/original.png',
                    'walk_r1/original.png'
        ]

        # arange faces on the canvas
        col = 0
        row = 0
        for face_path in self.Faces:
            self.arange(f'./original/{face_path}', col, row)
            if col > 1:
                row += 2
                col = 0
            else:
                col += 1
            self.copy_move_file(f'./original/{face_path}', f"{self.face_store}/{face_path[:-13]}")

    # function to arange images on the canvas
    def arange(self, face_path, col, row):
        face_logo = Image.open(f'{face_path}')
        face_logo = ImageTk.PhotoImage(face_logo)
        face_label = tk.Label(image=face_logo)
        face_label.image = face_logo
        face_label.grid(column=col, row=row)

    # function to move images to another folder
    def copy_move_file(self, img, target_dir):
        shutil.rmtree(target_dir)
        os.mkdir(target_dir)

        shutil.copy(img, target_dir)
    
    # function to generate buttons on the canvas
    def generate_buttons(self):
        # Buttons
        browse_text = [tk.StringVar() for i in range(len(self.Faces))]
        
        func = [
            BrowseFunc(self.root, browse_text[0], 0, 0, self.Faces[0],self.face_store),
            BrowseFunc(self.root, browse_text[1], 1, 0, self.Faces[1],self.face_store),
            BrowseFunc(self.root, browse_text[2], 2, 0, self.Faces[2],self.face_store),
            BrowseFunc(self.root, browse_text[3], 0, 2, self.Faces[3],self.face_store),
            BrowseFunc(self.root, browse_text[4], 1, 2, self.Faces[4],self.face_store),
            BrowseFunc(self.root, browse_text[5], 2, 2, self.Faces[5],self.face_store)
        ]

        browse_btn = [
            tk.Button(self.root, textvariable=browse_text[0], font='Raleway', bg='#20bebe', command=lambda:func[0].exe(), fg='black', height=2, width=15),
            tk.Button(self.root, textvariable=browse_text[1], font='Raleway', bg='#20bebe', command=lambda:func[1].exe(), fg='black', height=2, width=15),
            tk.Button(self.root, textvariable=browse_text[2], font='Raleway', bg='#20bebe', command=lambda:func[2].exe(), fg='black', height=2, width=15),
            tk.Button(self.root, textvariable=browse_text[3], font='Raleway', bg='#20bebe', command=lambda:func[3].exe(), fg='black', height=2, width=15),
            tk.Button(self.root, textvariable=browse_text[4], font='Raleway', bg='#20bebe', command=lambda:func[4].exe(), fg='black', height=2, width=15),
            tk.Button(self.root, textvariable=browse_text[5], font='Raleway', bg='#20bebe', command=lambda:func[5].exe(), fg='black', height=2, width=15),
        ]

        col = 0
        row = 1
        for i, face in enumerate(self.Faces):
            browse_text[i].set(f'{face[:-13]}')
            browse_btn[i].grid(column=col, row=row)
            if col > 1:
                row += 2
                col = 0
            else:
                col += 1

    # main
    def main(self):

        self.root.mainloop()

if __name__ == '__main__':
    app = APP()
    app.main()