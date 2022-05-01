import os

try:
    with open('config.yaml', encoding='utf-8') as f:
        for line in f:
            tuple = line.split()
            path = tuple[0]
            if not os.path.exists(path):
                os.mkdir(path)
            dirs = tuple[1].strip('[]').split(',')
            for dir in dirs:
                p = os.path.join(path, dir)
                if not os.path.exists(p):
                    os.mkdir(p)
            files = tuple[2].strip('[]').split(',')
            for file in files:
                if not file:
                    break
                with open(os.path.join(path, file), 'w+', encoding='utf-8') as g:
                    g.write('')
except (FileNotFoundError, EOFError) as e:
    print(f'Error directory: {e}')









