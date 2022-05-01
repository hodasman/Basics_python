import os
import shutil
from shutil import copy

root_dir = 'my_project' # Задаем корневую папку
main_templates = 'my_project/mainapp/templates' # Задаем путь куда будем копировать все найденные шаблоны
try:
    for root, dirs, files in os.walk(root_dir):
        for dir in dirs:
            if dir == 'templates':
                f = os.path.join(root, 'templates')
                if f != main_templates:
                    shutil.copytree(f, main_templates, dirs_exist_ok=True)
except (FileNotFoundError, EOFError) as e:
    print(f'Error directory: {e}')












