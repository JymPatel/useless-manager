import sys
from termcolor import colored



class Transaction:
    ...


class Person:
    ...


def main():
    task = get_task()
    
    if task == "version":
        print(f"manager.py\ncurrent version {current_version()[0]}.{current_version()[1]}")


def get_task():
    try: 
        task =  sys.argv[1]

        if task in ["-h", "--help", "help"]:
            return "help"
        if task in ["-v", "--version", "version"]:
            return "version"

        else: # else return error 102 in RED
            generated_error = "ERROR 102\nCould not find task provided\nTry manager.py --help"
            sys.exit(colored(generated_error, "red"))

    except IndexError: # no arguements given
        generated_error = "ERROR 101\nInsufficient argurments\nTry manager.py --help"
        sys.exit(colored(generated_error, "red"))




def current_version():
    major = 1
    minor = 1
    return [major, minor]

if __name__ == __name__:
    main()