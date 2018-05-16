import json
import sys
import os

studentInfoPath = "C:\\Users\Spectre\Documents\Programming\passwordManager\student_info.json"

class user_class():
    def __init__(self, name):
        self.name = name
        self.password = password

    @classmethod
    def create_new_user(clf):
        newUserCreated = False
        while newUserCreated is False:
            name = input("name: ")
            confermation = input(f"your name is: {name}. Is this correct?")

            if confermation == 'Y' or confermation == 'y' or confermation == 'yes' or confermation == 'Yes' or confermation == 'YES':
                password = input("password: ")
                confermation = input("retype password: ")
                if confermation == password:
                    print("all done")
                    newUserCreated = True
                    user_class.add_to_user_list(name, password)
                    user_class.create_user_file(name)
                else:
                    print("your passwords do not match")
            else:
                pass

    def add_to_user_list(name, password):
        load_file()
        usersInFile = fileLoaded["users"]

        usersInFile.update({
            name:{
                "userName": name,
                "password": password
            }
        })

        with open(studentInfoPath, 'w') as outfile:
            json.dump(fileLoaded, outfile)

        outfile.close()
    
    def create_user_file(username):
        fileName = username + ".json"
        f = open(fileName, 'w')
        data = {
        }
        json.dump(data, f)

def load_file():
    global fileLoaded
    
    fileSize = os.path.getsize(studentInfoPath)

    if fileSize > 0:
        f = open(studentInfoPath, 'r')
        fileLoaded = json.load(f)
        f.close()
        return

    else:
        f = open(studentInfoPath, 'w')
        data = {
            "users": {

            }
        }
        json.dump(data, f)
        f.close()
        return


def login():
    userName = input("user name: ")

    if userName == "new user":
        user_class.create_new_user()
    
    elif userName == "quit" or userName == 'q':
        sys.exit(0)

    else:
        password = input("password: ")
        listOfUsers = fileLoaded["users"].keys()
        userInList = userName in listOfUsers

        if userInList is True:
            name = fileLoaded["users"][userName]["userName"]
            if userName == name:
                    passwrd = fileLoaded["users"][userName]["password"]
                    if password == passwrd:
                        print("you're in!")
                    print("Username or password incorrect")
        else:
            print("Username or password incorrect")
    
    return True

def mainMenu():
    print("main menu")

def run(fileIsLoaded):

    while True:
        if not fileIsLoaded:
            load_file()
            login()
        
        else:
            mainMenu()



run(False)
