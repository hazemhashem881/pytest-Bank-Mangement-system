import pickle
import pathlib
import os


class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''

    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
        

def depositAndWithdraw(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            mylist = pickle.load(infile)
        for item in mylist:
            if item.accNo == num1:
                if num2 == 1:
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updated")
                elif num2 == 2:
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit:
                        item.deposit -= amount
                        print("Your account is updated")
                    else:
                        print("Amount is large! *ERROR 404*")
        with open('accounts.data', 'wb') as outfile:
            pickle.dump(mylist, outfile)
    else:
        print("No records to search")