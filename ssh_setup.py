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

class SSH():
    def __init__(self, config='config.yaml'):
        ############# 設定
        with open(config) as file:
            yml = yaml.load(file, Loader=Loader)
            self.ip_address = yml['ip_address']
            self.my_port = yml['port']
            self.my_username = yml['user']
            self.my_password = yml['pass']

        #############

        ############# 実行コマンド
            self.cmd = 'ls'
        ############# 実行コマンド
    
    def setup(self):
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
            stdin, stdout, stderr = ssh.exec_command(self.cmd)

            # コマンド実行後に標準入力が必要な場合
            # stdin.write('password\n')
            # stdin.flush()

            # 実行結果を表示
            for o in stdout:
                print('[std]', o, end='')
            for e in stderr:
                print('[err]', e, end='')
