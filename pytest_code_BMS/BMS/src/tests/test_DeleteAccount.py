import pytest
import pickle
import os
import pathlib
from BMS.src.DeleteAccount import Account, deleteAccount

@pytest.fixture
def setup_accounts_file():
    # Create a sample accounts.data file for testing
    accounts = [
        Account(),
        Account(),
        Account()
    ]
    accounts[0].accNo = 1
    accounts[0].name = 'Hazem'
    accounts[0].deposit = 1000
    accounts[0].type = 'C'

    accounts[1].accNo = 2
    accounts[1].name = 'Ahmed'
    accounts[1].deposit = 500
    accounts[1].type = 'S'

    accounts[2].accNo = 3
    accounts[2].name = 'Mohamed'
    accounts[2].deposit = 2000
    accounts[2].type = 'c'

    with open('accounts.data', 'wb') as f:
        pickle.dump(accounts, f)
    yield
    # Clean up the test file after the test is done
    os.remove('accounts.data')

def test_deleteAccount(setup_accounts_file):
    # Test deleting an existing account
    deleteAccount(2)
    with open('accounts.data', 'rb') as f:
        accounts = pickle.load(f)
    assert len(accounts) == 2
    assert accounts[0].accNo == 1
    assert accounts[1].accNo == 3

    # Test deleting a non-existing account
    deleteAccount(4)
    with open('accounts.data', 'rb') as f:
        accounts = pickle.load(f)
    assert len(accounts) == 2
    assert accounts[0].accNo == 1
    assert accounts[1].accNo == 3