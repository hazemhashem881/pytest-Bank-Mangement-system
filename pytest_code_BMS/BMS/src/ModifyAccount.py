import pickle
import os
import pathlib

class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
        


def modifyAccount(num, name=None, account_type=None, deposit=None, filename=None):
    file = pathlib.Path(filename or "accounts.data")
    if file.exists():
        with open(str(file), 'rb') as infile:
            oldlist = pickle.load(infile)
        os.remove(str(file))
        for item in oldlist:
            if item.accNo == num:
                item.name = name or input("Enter the Account Holder Name: ")
                item.type = account_type or input("Enter the Account Type (C/S): ")
                item.deposit = deposit or int(input("Enter the Amount: "))
        with open('newaccounts.data', 'wb') as outfile:
            pickle.dump(oldlist, outfile)
        os.rename('newaccounts.data', str(file))