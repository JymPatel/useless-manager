#!/usr/bin/python3
# by @JymPatel
# this code is licensed under GPL v3 License
print("this code is licensed under GPL v3 License\n")
manager_version = "0.0.23"

import sys
from termcolor import colored
import scripts.functions as fn
import scripts.load_save as ldsv


arg = sys.argv[1:]
# get data & profiles
try:
    [balance_sheet, profiles, settings] = ldsv.load_data()
except ValueError:
    print("would you like to reset data")


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

# reset settings
elif (task == "-rs") or (task == "--reset-settings"):
    fn.reset_settings()

# === adding amount ===
elif (task == "-ab") or (task == "--add-balance"):
    username = arg[1]
    if (len(arg) < 3): # check for sufficient arguements
        print(colored("insufficient arguements", "red"), "for -a command need", colored("-a *user *amount", "red"))
        fn.help()
    else:
        # == updating data ==
        if username in balance_sheet:
            balance_sheet[username] += int(arg[2])
        else:
            balance_sheet[username] = int(arg[2])
        new_amnt = balance_sheet[username]
        print(username, ":", colored(new_amnt, "red" if new_amnt > 0 else "green"))
        # == send email ==
        if (username in profiles) and (profiles[username][2] == True):
            if settings["default_email"] == None:
                sender_email = input("senders email: ")
            else:
                sender_email = settings["default_email"]
            fn.send_mail(balance_sheet[username], profiles[username][0], profiles[username][1], sender_email, input("password : "))
        else:
            print("no profile found for", username, "would you like to create one and send mail")


# save data
ldsv.save_data(balance_sheet, profiles, settings)
