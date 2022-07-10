# this code is licensed under GNU General Public License v3 (https://github.com/JymPatel/useless-manager/blob/master/LICENSE)

import sys
from termcolor import colored


# defining global variables (will be overwrite by main() at initial run)
users = [] # stores identities of users
transactions = [] # stores all transactions done


class Transaction:
    ...


class Person:
    def __init__(self, first, last, middle, entered_ID, balance=0):
        self.balance = balance
        # set Person name
        if middle == "":
            self.name = first + " " + last
        else:
            self.name = first + " " + middle + " " + last
        # set Person id
        try:
            self.ID = entered_ID
        except ValueError:
            raise ValueError("user ID already taken!")

    # lock ID of person not to duplicate
    @property
    def ID(self):
        return self.id
    
    @ID.setter
    def ID(self, ID):
        if ID not in [user.id for user in users]:
            self.id = ID
        else:
            raise ValueError("user ID already taken!")



def main():
    task = get_task()
    
    if task == "version":
        print(f"manager.py\ncurrent version {current_version()}")
    elif task == "help":
        get_help()
    elif task == "newaccount":
        users.append(create_user())
        print(colored(f"created account for {users[-1].name} with UNIQUE ID {users[-1].ID} and balance {users[-1].balance}", "green"))
    
    # smooth end
    print(colored("\nthis code is licensed under GNU Public License V3\nget this code at https://github.com/JymPatel/useless-manager", "blue"))


def get_task(): # returns task as string from command line input
    try: 
        task =  sys.argv[1]

        if task in ["-h", "--help", "help"]:
            return "help"
        elif task in ["-v", "--version", "version"]:
            return "version"
        elif task == "newaccount":
            return "newaccount"

        else: # else return error 102 in RED
            generated_error = "ERROR 102\nCould not find task provided\nTry manager.py --help"
            sys.exit(colored(generated_error, "red"))

    except IndexError: # no arguements given
        generated_error = "ERROR 101\nInsufficient argurments\nTry manager.py --help"
        sys.exit(colored(generated_error, "red"))


def get_help(): # opens help doc
    print(colored("opening docs/help ...", "yellow"))
    print(open("./docs/help.txt", 'r').read())


def create_user(): # returns user of type Person created by taking input
    first = input("First Name: ")
    middle = input("Middle Name: ")
    last = input("Last Name: ")
    while True:
        try:
            unique_id = input("create UNIQUE ID: ")

            if unique_id == "": # empty ID
                print(colored("you can't use empty string!", "red"))
                continue

            user = Person(first, last, middle, unique_id)
            break

        except ValueError:
            print(colored("UNIQUE ID already taken, try another!", "red"))
            continue
    return user



def current_version(): # returns string of version
    major = 1
    minor = 1
    return str(major) + "." + str(minor)

if __name__ == __name__:
    main()
