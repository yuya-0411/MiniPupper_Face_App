# yaml>5.x :: you need run yaml.load and yaml.dump with Loader and Dumper respectively
# https://pyyaml.org/wiki/PyYAMLDocumentation
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# LOAD
with open('config.yaml') as file:
    yml = yaml.load(file, Loader=Loader)
    for key in yml:
        print(f"{key} = {yml[key]}  {type(yml[key])}")

# DUMP
yml = {
        'ip_address':'192.168.13.17',
        'port':'22',
        'user':'ubuntu',
        'pass':'mangdang',
        'cmd':'ls -al',
        'folder_path':'path1',
        'minipupper_folder':'path2'
        }
with open('test_out.yaml', 'w') as file:
    yaml.dump(yml, file, Dumper=Dumper)