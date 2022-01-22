import subprocess

# 'D:\MiniPupper\MiniPupper_Face'
def face_setup(path):
    cmd = f'{path[0:2]} && cd {path} && git add . && git commit -m "modified" && git push origin main'
    print(cmd)
    # subprocess.Popen(cmd, shell=True)