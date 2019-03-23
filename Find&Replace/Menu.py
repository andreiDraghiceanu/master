
from Script_Methods import *

class Menu:
    def __init__(self):
        pass

    print("Please choose an option: ")
    print("1 - List Tree Directories")
    print("2 - Replace Folder Names")
    print("3 - Replace File Names")
    print("4 - Replace Into Files")
    print("5 - Exit")


    @staticmethod
    def main_menu(path):
        choice = input("Choose an option: ")
        print(choice)
        choices = list()
        for i in choice:
            choices.append(i)
            while " " in choices:
                choices.remove(" ")
        for i in range(len(choices)):
            choices[i] = int(choices[i])
        for i in choices:
            if i == 1:
                init = Script_Methods()
                init.list_tree(path)
                print("\n")
            elif i == 2:
                init = Script_Methods()
                init.replace_folder_names(path)
            elif i == 3:
                init = Script_Methods()
                init.replace_file_names(path)
            elif i == 4:
                init = Script_Methods()
                init.replace_in_file(path)
                break
            elif i == 5:
                return
            else:
                print("Please choose a valid option: 1-4!")
                reinitialize = Menu()
                return reinitialize.main_menu(path)
        return






# path = "C:\\Users\\andre\\Desktop\\Test"
# m = Menu(object)
# m.main_menu(path)



