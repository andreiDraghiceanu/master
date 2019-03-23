
import sys
from pathlib import Path
import os

class Script_Methods():
    def __init__(self):
        pass


    def _find_and_replace(self):
        find = input("Find: ")
        replace = input("Replace: ")
        return find, replace


    # list directories and sub-directories beneath root
    def list_tree(self, path):
        if Path(path).exists() == 0:
            print("Path is not valid!")
        else:
            for root, dirs, files in os.walk(path, topdown=True):
                for name in files:
                    print(os.path.join(root, name))
                for name in dirs:
                    print(os.path.join(root, name))

    # rename sub-directories as a separate walkthrough
    def replace_folder_names(self, path):
        find = input("Find: ")
        replace = input("Replace: ")
        if Path(path).exists() == 0:
            print("Path is not valid!")
        else:
            for root, dirs, filenames in os.walk(path, topdown=False):
                dirs[:] = [d for d in dirs if d != '.git']  # skip .git dirs
                for thedir in dirs:
                    if find in thedir:
                        path1 = os.path.join(root, thedir)
                        path2 = os.path.join(root, thedir.replace(find, replace))
                        os.rename(path1, path2)
                        print("dir: " + path1 + "  renamed to: " + path2)

    # walk through the directory from bottom up
    def replace_in_file(self, path):
        if Path(path).exists() == 0:
            print("Path is not valid!")
        else:
            find = input("Find: ")
            replace = input("Replace: ")
            for root, dirs, filenames in os.walk(path, topdown=False):
                dirs[:] = [d for d in dirs if d != '.git']  # skip .git dirs
                for filename in filenames:
                    if filename != "replaceall.py":
                        # search and replace within files themselves
                        filepath = os.path.join(root, filename)
                        with open(filepath) as f:
                            s = f.read()
                            s = s.replace(find, replace)
                            with open(filepath, "w") as f:
                                f.write(s)

    # rename files (ignoring file extensions)
    def replace_file_names(self, path):
        if Path(path).exists() == 0:
            print("Path is not valid!")
        else:
            find = input("Find: ")
            replace = input("Replace: ")
            for root, dirs, filenames in os.walk(path, topdown=False):
                dirs[:] = [d for d in dirs if d != '.git']  # skip .git dirs
                for filename in filenames:
                    filename_split = os.path.splitext(filename)  # filename and extensionname (extension in [1])
                    filename_zero = filename_split[0]
                    extension = filename_split[1]
                    if find in filename_zero and filename != "replaceall.py":
                        path1 = os.path.join(root, filename)
                        path2 = os.path.join(root, filename_zero.replace(find, replace) + extension)
                        os.rename(path1, path2)
                        print("file: " + path1 + "  renamed to: " + path2)

# path = "C:\\Users\\andre\\Desktop\\Test\\Mue"
# init = Script_Methods()
# init.list_tree(path)



