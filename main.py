# by @JymPatel
# this code is licensed under GPL v3 License
print("this code is licensed under GPL v3 License\n")


import sys
import os
import pickle
from termcolor import colored
import scripts.functions as fn
import scripts.load_save as ldsv


arguments = sys.argv[1:]
# get data & profiles if path exists
[balance_sheet, profiles] = ldsv.load_data()


# check number of arguements & get task to do
if (len(arguments) < 1):
    print("insufficient arguements, opening help file ...")
    fn.help()
    exit()
task = arguments[0].lower()


# help
if (task == "-h") or (task == "--help"):
    print("opening docs/help.txt ...")
    fn.help()

# reset data
elif (task == "-rd") or (task == "--reset-data"):
    balance_shee = fn.reset_data()

# reset profiles
elif (task == "-rp") or (task == "--reset-profiles"):
    fn.reset_profiles()


# === adding amount ===
elif (task == "-ab") or (task == "--add-balance"):
    if (len(arguments) < 3): # check for sufficient arguements
        print(colored("insufficient arguements", "red"), "for -a command need", colored("-a *user *amount", "red"))
        fn.help()
    else:
        # == updating data ==
        if arguments[1] in balance_sheet:
            balance_sheet[arguments[1]] += int(arguments[2])
        else:
            balance_sheet[arguments[1]] = int(arguments[2])
        new_amnt = balance_sheet[arguments[1]]
        print(arguments[1], ":", colored(new_amnt, "red" if new_amnt > 0 else "green"))
        # == send email ==
        if (arguments[1] in profiles):
            if len(arguments) == 6:
                fn.send_mail(arguments[1], new_amnt)
        else:
            print("no profile found for", arguments[1], "would you like to create one and send mail")




# save data
ldsv.save_data(balance_sheet, profiles)