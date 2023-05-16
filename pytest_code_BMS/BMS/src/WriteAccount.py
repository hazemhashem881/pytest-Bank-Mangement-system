import pathlib
import pickle
import os

class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    
    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount(minimum 500 for Saving and 1000 for current: "))
        print("\n\nCongrats! New Account Created")

def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')