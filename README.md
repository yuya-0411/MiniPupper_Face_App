# MiniPupper_Face_App for Windows

MiniPupper is a robot from MangDang.
This robot has some types of facial expression.

### you can change facial expression through this app!

## STEP1: setup environment
Though this app, you can change its face via github as long as you can access computer on MiniPupper by using ssh.

so you need as follows:
- create one repository on github required to be public
- setting ssh conncting between you computer and the robot

## STEP2: setup app
In this repository you can't do "git push" easily, so you need to copy these files to your new repository in order to use github as something like image server.

so you need as follows:
- git clone this repository on your computer
    - if you wanna run python file, choose main branch, please
    - if you wanna use just app easily, choose app branch, please
        - you don't need have python and any environment
- copy all files except "__pycache__" folder to your repository you created the above
- modify config.yaml file

## STEP3: modify config.yaml
config.yaml is a file for setting parameters to use this app on your computer.

config.yaml has some parameters as follows:
- ip_address: "ip address to connect ssh"
- port: "port should be '22' unless you change manually"
- user: "user name for computer on MiniPupper"
- pass: "ubuntu password"
- repository: "local repository path, absolute path is recommended"
- repository: "local repository name, absolute path is recommended"
- face_store: "you don't need to change"
- first_use: "for first use, please set False"

## STEP4: use app
- if you choose main branch, run the below.

```:install libraries
pip install yaml, paramiko
```
```:launch app.py
python Face_app.py
```

- if you choose app branch, you launch the exe file (Face_app.exe)

https://user-images.githubusercontent.com/83892604/151650197-20d9f2d5-d321-4403-bb90-dbe6e1edc59d.mp4

https://user-images.githubusercontent.com/83892604/151650208-b5f606b7-d364-4c7e-ad28-b4ea24f4f645.mp4


## CAUTION!
the size for images is recommended to be 320x240 because LCD on MiniPupper is 320x240.
