# by @JymPatel
# this code is licensed under GPL v3 License
print("this code is licensed under GPL v3 License\n")


import sys
import os
import pickle
from termcolor import colored
import scripts.functions as fn
import scripts.load_save as ldsv


arg = sys.argv[1:]
# get data & profiles
[balance_sheet, profiles] = ldsv.load_data()
if balance_sheet == 1:
    print("sorry! but we can't find [balance_sheet] file :(")
    print("try",  colored("main.py --reset-balance", "green"), "to reset Balance Sheet")
elif balance_sheet == 2:
    print("sorry! but we can't find [profiles] file :(")
    print("try",  colored("main.py --reset-profiles", "green"), "to reset profiles")


# check number of arguements & get task to do
if (len(arg) < 1):
    print("insufficient arguements, opening help file ...")
    fn.help()
    exit()
task = arg[0].lower()


# help
if (task == "-h") or (task == "--help"):
    print("opening docs/help.txt ...")
    fn.help()

# reset data
elif (task == "-rb") or (task == "--reset-balance"):
    balance_sheet = fn.reset_data()

# reset profiles
elif (task == "-rp") or (task == "--reset-profiles"):
    fn.reset_profiles()


# === adding amount ===
elif (task == "-ab") or (task == "--add-balance"):
    if (len(arg) < 3): # check for sufficient arguements
        print(colored("insufficient arguements", "red"), "for -a command need", colored("-a *user *amount", "red"))
        fn.help()
    else:
        # == updating data ==
        if arg[1] in balance_sheet:
            balance_sheet[arg[1]] += int(arg[2])
        else:
            balance_sheet[arg[1]] = int(arg[2])
        new_amnt = balance_sheet[arg[1]]
        print(arg[1], ":", colored(new_amnt, "red" if new_amnt > 0 else "green"))
        # == send email ==
        if (arg[1] in profiles):
            if len(arg) == 6:
                fn.send_mail(arg[1], new_amnt)
        else:
            print("no profile found for", arg[1], "would you like to create one and send mail")


# save data
ldsv.save_data(balance_sheet, profiles)