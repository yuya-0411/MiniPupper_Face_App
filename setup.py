"""
Pythonからssh接続を行うためには paramiko というライブラリが必要
pip install paramiko
"""
# yaml>5.x :: you need run yaml.load and yaml.dump with Loader and Dumper respectively
# https://pyyaml.org/wiki/PyYAMLDocumentation
from ipaddress import ip_address
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import paramiko
import subprocess
from time import time

class SETUP():
    def __init__(self, config_yaml='config.yaml'):
        ############# 設定
        with open(config_yaml) as file:
            yml = yaml.load(file, Loader=Loader)
            self.ip_address = yml['ip_address']
            self.my_port = yml['port']
            self.my_username = yml['user']
            self.my_password = yml['pass']
            self.push_path = yml['repository']
            self.face_store = yml['face_store']
            # self.pull_path = yml['repository_on_minipupper']
        #############

        ############# 実行コマンド
        # before running: git clone (or git pull) on home directory
        # run: python MiniPupper_Face/face_change.py
        # self.cmd = 'cd && git clone (or git pull) && python MiniPupper_Face_App/face_change.py'
        self.cmd = 'cd MiniPupper_Face_App && git pull && python3 face_change.py'
        ############# 実行コマンド
    def folder(self):
        return self.face_store
    def ssh_setup(self):
        # with付きで準備することで，最後自動でssh.close()
        with paramiko.SSHClient() as ssh:
            # 初回ログイン時に「Are you sure you want to continue connecting (yes/no)?」と
            # きかれても問題なく接続できるように。
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # ssh接続
            ssh.connect(self.ip_address,
                        port=self.my_port,
                        username=self.my_username,
                        password=self.my_password)

            # コマンド実行
            # before running: git clone (or git pull) on home directory
            # run: python MiniPupper_Face/face_change.py
            stdin, stdout, stderr = ssh.exec_command(self.cmd)

            # コマンド実行後に標準入力が必要な場合
            # stdin.write('password\n')
            # stdin.flush()

            # 実行結果を表示
            for o in stdout:
                print('[std]', o, end='')
            for e in stderr:
                print('[err]', e, end='')
    # 'D:\MiniPupper\MiniPupper_Face'
    def face_setup(self):
        cmd = f'{self.push_path[0:2]} && cd {self.push_path} && git add . && git commit -m "modified" && git push origin main'
        print(cmd)
        subprocess.Popen(cmd, shell=True)
        sleep(3)
        self.ssh_setup()