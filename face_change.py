#! /usr/bin/env python3
"""
Change Face Easily for MiniPupper

###
before running: git clone (or git pull) on home directory
run: python MiniPupper_Face/face_change.py
###

STEP1: get information of images for faces in MiniPupper_face folder
STEP2: rename them into applied names for MiniPupper
STEP3: mv them to ~/Robotics/QuadrupedRobot/Mangdang/LCD/cartoons/
STEP4: cd ~/Robotics/QuadrupedRobot/StanfordQuadruped/
STEP5: sudo systemctl stop robot
STEP6: sudo systemctl start robot

"""

import glob
import shutil
import subprocess

folders = [
            "./Faces/logo",
            "./Faces/notconnect",
            "./Faces/sleep",
            "./Faces/turnaround",
            "./Faces/walk",
            "./Faces/walk_r1"
]
names = [
            "logo.png",
            "notconnect.png",
            "sleep.gif",
            "turnaround.png",
            "walk.png",
            "walk_r1.png"
]

type = ['jpg', 'png', 'gif']

img_list = []
name_list = []

COPY_PATH = "../Robotics/QuadrupedRobot/Mangdang/LCD/cartoons"

cmd1 = "sudo systemctl stop robot"
cmd2 = "sudo systemctl start robot"

for expantion in type:
    for n, folder in enumerate(folders):
        if len(glob.glob(f"{folder}/*.{expantion}"))!=0:
            img_list.append(glob.glob(f"{folders[n]}/*.{expantion}")[0])
            name_list.append(names[n])
        else:
            pass

[shutil.copy(f'{img_path}', f'{COPY_PATH}/{name_list[n]}') for n, img_path in enumerate(img_list)]

subprocess.run(cmd1, shell=True)
subprocess.run(cmd2, shell=True)

print("Finished!!")