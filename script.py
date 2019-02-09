import os

root="complete directory of the folder"
count = 0
def clear_files(root,extension):
    for path, subdirs, files in os.walk(root):
        for name in files:
            if name.endswith('.'+ extension):
                p=os.path.join(path, name)
                os.remove(p)
                global count
                count = count+1
                print(name)
                
root = input("Enter the dir: ")
extension = input("Enter the extension of the files to remove: ")
clear_files(root,extension)
print(str(count)+" files are deleted")