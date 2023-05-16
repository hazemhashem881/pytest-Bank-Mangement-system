import pytest
import os.path
import pickle
from unittest.mock import patch
from BMS.src.WriteAccount import writeAccountsFile, Account


@pytest.fixture()
# Create an instance of the Account class
def test_account1():
    # Set the account attributes
    account = Account()
    account.accNo = 1234
    account.name = "hazem hashem"
    account.type = "C"
    account.deposit = 500
    return account

@pytest.fixture()
def test_account2():
    account = Account()
    account.accNo = 12345
    account.name = "mohamed ahmed"
    account.type = "S"
    account.deposit = 1000
    return account

# Using the pytest fixture decorator to define a fixture function
@pytest.fixture()
def test_data_file(test_account1,test_account2):
    file_name = "test_accounts.data"
    with open(file_name, "wb") as f:
        pickle.dump([test_account1,test_account2], f)
    yield file_name  # Yielding the file name to be used by the tests
    os.remove(file_name)


def test_writeAccountsFile(test_account1, test_account2, test_data_file):
    # Patching the "input" function to provide predefined values for user input
    with patch("builtins.input", side_effect=[1234, "hazem hashem", "C", 500]):
    # Calling the writeAccountsFile function with test_account1
        writeAccountsFile(test_account1)
    # Patching the "input" function again for test_account2
    with patch("builtins.input", side_effect=[12345,"mohamed ahmed","S",1000]):
        writeAccountsFile(test_account2)

    with open("test_accounts.data", "rb") as f:
        accounts = pickle.load(f)


#----------------------- Test the frist account------------
    assert len(accounts) == 2
    assert accounts[-2].accNo == 1234
    assert accounts[-2].name == "hazem hashem"
    assert accounts[-2].type == "C"
    assert accounts[-2].deposit == 500

#----------------------- Test the second account------------

    assert accounts[-1].accNo == 12345
    assert accounts[-1].name == "mohamed ahmed"
    assert accounts[-1].type == "S"
    assert accounts[-1].deposit == 1000