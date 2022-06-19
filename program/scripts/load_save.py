from distutils import file_util
import os
import pickle
from termcolor import colored


def load_data():
    _path = "./data/balance_sheet"
    data = []
    if os.path.exists(_path):
        _datafile = open(_path, "rb")
        data.append(pickle.load(_datafile))
        _datafile.close()
    else:
        return [1, 1, 1]

    _path = "./data/profiles"
    if os.path.exists(_path):
        _datafile = open(_path, "rb")
        data.append(pickle.load(_datafile))
        _datafile.close()
    else:
        return[2, 2, 2]

    _path = "./data/settings"
    if os.path.exists(_path):
        _datafile = open(_path, "rb")
        data.append(pickle.load(_datafile))
        _datafile.close()
    else:
        return [3, 3, 3]
    
    return data


def save_data(balance_sheet, profiles, settings):
    file = open("data/balance_sheet", "wb")
    pickle.dump(balance_sheet, file)
    file.close()
    file = open("data/profiles", "wb")
    pickle.dump(profiles, file)
    file.close()
    file = open("data/settings", "wb")
    pickle.dump(settings, file)
    file.close()
    print("TODO")
