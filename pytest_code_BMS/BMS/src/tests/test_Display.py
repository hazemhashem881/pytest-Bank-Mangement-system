import pytest
import pickle
import os.path
from unittest.mock import patch
from BMS.src.WriteAccount import writeAccountsFile, Account
from BMS.src.Display import displaySp,Account,displayAll

"""
    
                        
    
    
    
                        The line 59 and 65 don't work
    
    
    
    
    
    
"""




@pytest.fixture()
def test_account1():
    account = Account()
    account.accNo = 1234
    account.name = "hazem hashem"
    account.type = "C"
    account.deposit = 500
    return account

@pytest.fixture()
def test_data_file(test_account1):
    file_name = "test_accounts.data"
    with open(file_name, "wb") as f:
        pickle.dump([test_account1], f)
    yield file_name
    os.remove(file_name)


def test_writeAccountsFile(test_account1, test_data_file):
    with patch("builtins.input", side_effect=[1234, "hazem hashem", "C", 500]):
        writeAccountsFile(test_account1)
    with open("test_accounts.data", "rb") as f:
        accounts = pickle.load(f)





def test_displaySp(capsys, test_account1, test_data_file):
    # call the function with input value and capture the output
    displaySp(1234)
    captured = capsys.readouterr()
    # assert captured.out == "Your account Balance is =  " + str(test_account1.deposit) + "\n"
    
    # test displayAll function 

    displayAll()
    captured = capsys.readouterr()
    # assert captured.out == print(test_account1.accNo," ",test_account1.name, " ",test_account1.type," ",test_account1.deposit )