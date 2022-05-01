import os

config = ('my_project', ['settings', 'mainapp', 'adminapp', 'authapp'], [])
if not os.path.exists(config[0]):
    os.mkdir(config[0])
os.chdir(config[0])
for item in config[1]:
    if not os.path.exists(item):
        os.mkdir(item)