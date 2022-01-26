"""
you need library "paramiko" in order to connect ssh from python
pip install paramiko
"""
# yaml>5.x :: you need run yaml.load and yaml.dump with Loader and Dumper respectively
# https://pyyaml.org/wiki/PyYAMLDocumentation
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import paramiko
import subprocess

class SETUP():
    def __init__(self, config_yaml='config.yaml'):
        ############# 設定
        with open(config_yaml) as file:
            yml = yaml.load(file, Loader=Loader)
            self.ip_address = yml['ip_address']
            self.my_port = yml['port']
            self.my_username = yml['user']
            self.my_password = yml['pass']
            self.repository = yml['repository']
            self.face_store = yml['face_store']
            self.first_use = yml['first_use']
        #############

    def folder(self):
        return self.face_store

    def ssh_setup(self):
        # use 'with' to run ssh.close() automatically
        with paramiko.SSHClient() as ssh:
            # you don't to answer "Are you sure you want to continue connecting (yes/no)?"
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # access the computer on MiniPupper via ssh
            ssh.connect(self.ip_address,
                        port=self.my_port,
                        username=self.my_username,
                        password=self.my_password)

            ############# command run on computer of MiniPupper
            if self.first_use:
                self.cmd = f'cd {self.repository} && git checkout app && git pull && python3 face_change.py'
            else:
                self.first_use = True
                self.cmd = f'cd {self.repository} && git checkout app && git clone && python3 face_change.py'
                yml = {
                    'ip_address':self.ip_address,
                    'port':self.my_port,
                    'user':self.my_username,
                    'pass':self.my_password,
                    'repository':self.repository,
                    'face_store':self.face_store,
                    'first_use':self.first_use
                    }
                with open('config.yaml', 'w') as file:
                    yaml.dump(yml, file, Dumper=Dumper)
            #############

            # run the command
            stdin, stdout, stderr = ssh.exec_command(self.cmd)
            

            # show the result
            for o in stdout:
                print('[std]', o, end='')
            for e in stderr:
                print('[err]', e, end='')
    
    # setup images for faces in
    def face_setup(self):
        cmd = f'{self.repository[0:2]} && cd {self.repository} && git checkout app && git add . && git commit -m "modified" && git push origin app'
        subprocess.run(cmd, shell=True)

        self.ssh_setup()