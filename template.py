import os

dirs = [
    os.path.join('data', 'raw'),
    os.path.join('data', 'processed'),
    'data_given',
    'notebooks',
    'saved_models',
    'src'
]
for dir in dirs:
    os.makedirs(dir, exist_ok=True)
    with open(os.path.join(dir, '.gitkeep'), 'w') as f: # keep gitignore file so that it can be pushed to git even if empty repo
        pass 

files = [
    'dvc.yaml',
    'params.yaml',
    '.gitignore', # files dont want to push to git
    os.path.join('src', '__init__.py')

]

for file in files:
    with open(file, 'w') as f:
        pass