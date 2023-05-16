import os
import pickle
import pathlib
from BMS.src.ModifyAccount import Account, modifyAccount

def test_modifyAccount():
    # Create a temporary file for testing
    test_file = pathlib.Path("test_accounts.data")
    
    # Create some test account data
    accounts = [
        Account(),
        Account(),
        Account()
    ]
    accounts[0].accNo = 1
    accounts[0].name = 'Hazem'
    accounts[0].deposit = 100
    accounts[0].type = 'C'
    
    accounts[1].accNo = 2
    accounts[1].name = 'Hashem'
    accounts[1].deposit = 200
    accounts[1].type = 'S'
    
    accounts[2].accNo = 3
    accounts[2].name = 'Ahmed'
    accounts[2].deposit = 300
    accounts[2].type = 'C'
    
    # Write the test account data to the temporary file
    with open(test_file, 'wb') as f:
        pickle.dump(accounts, f)
    
    # Modify account #2 in the temporary file
    
    modifyAccount(2, name='New Name', account_type='C', deposit=500, filename=str(test_file)) 
    
    # Read the modified account data from the temporary file
    with open(test_file, 'rb') as f:
        new_accounts = pickle.load(f)
    
    # Verify that the account details were modified correctly
    assert new_accounts[1].name == 'New Name'
    assert new_accounts[1].type == 'C'
    assert new_accounts[1].deposit == 500