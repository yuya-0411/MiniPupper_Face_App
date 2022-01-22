from tkinter import filedialog

# フォルダパスの取得
fld = filedialog.askdirectory(initialdir = dir) 

print(fld)

# ファイルパスの取得
typ = [
        ('PNG','*.png'),
        ('JPG','*.jpg'),
        ('GIF','*.gif')
        ] 
dir = 'C:'
fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir) 

print(fle)
