import os

root="complete directory of the folder"

def clear_files(root,extension):
    for path, subdirs, files in os.walk(root):
        for name in files:
            if name.endswith('.'+ extension):
                p=os.path.join(path, name)
                os.remove(p)
                print(name)
                
clear_files(root,'vtt')