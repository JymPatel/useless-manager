import os
import pickle
from termcolor import colored


def load_data():
    _path = "./data/main_data"
    data = []
    if os.path.exists(_path):
        _datafile = open(_path, "rb")
        data.append(pickle.load(_datafile))
        _datafile.close()
    else:
        print("sorry! but we can't find data file :(")
        print("try",  colored("main.py --reset-data", "green"), "to reset data")

    _path = "./data/main_profiles"
    if os.path.exists(_path):
        _datafile = open(_path, "rb")
        data.append(pickle.load(_datafile))
        _datafile.close()
    else:
        print("sorry! but we can't find data file :(")
        print("try",  colored("main.py --reset-data", "green"), "to reset data")
    
    return data


def save_data(balance_sheet, profiles):
    print("TODO")
