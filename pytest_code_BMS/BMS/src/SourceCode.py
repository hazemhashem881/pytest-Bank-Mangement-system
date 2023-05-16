import sys
from Display import displayAll,displaySp
from WriteAccount import writeAccount
from DepositAndWithdraw import depositAndWithdraw
from DeleteAccount import deleteAccount
from ModifyAccount import modifyAccount
    
def intro():
    if sys.stdin.isatty():
        print("Welcome to MyBank. Please enter your name:")
        name = input().strip()
        print(f"Hi {name}, what would you like to do today?")
    else:
        # standard input is not a terminal, so skip the interactive intro
        pass






ch=''
num=0
intro()

while ch != 8:
    print("\tMAIN MENU")
    print("\t1. New Account")
    print("\t2. Deposit Amount")
    print("\t3. Withdraw Amount")
    print("\t4. Balance Enquiry")
    print("\t5. All Account Holder List")
    print("\t6. Close an Existing Account")
    print("\t7. Modify Information of any Account")
    print("\t8. Exit")
    print("\tSelect Your Option from 1 to 8")
    ch = input()
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
    elif ch == '5':
        displayAll();
    elif ch == '6':
        num =int(input("\tEnter The account No. : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tThanks for using bank managemnt system")
        break
    else :
        print("Please enter the valid field")
    
    ch = input("Press <ENTER> ") 
    
