import os

# root: It is the root is the complete path of the folder from which you want to delete the files
# extension: It is the extension of the file to be deleted eg: srt,vtt,txt..
# This program deletes all the files for that particular extension, even from all the subfolders.

def clear_files(root,extension):
    for path, subdirs, files in os.walk(root):
        for name in files:
            if name.endswith('.'+ extension):
                p=os.path.join(path, name)
                os.remove(p)
                global count 
                count = count+1
                print(name)
                
if __name__ == "__main__":
    count = 0
    root = input("Enter the dir: ")
    extension = input("Enter the extension of the files to remove: ")
    clear_files(root,extension)
    print(str(count)+" files are deleted")
