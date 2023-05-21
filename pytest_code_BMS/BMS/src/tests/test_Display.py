from unittest.mock import patch,MagicMock
from BMS.src.WriteAccount import writeAccountsFile, Account
from BMS.src.Display import displaySp,Account,displayAll

"""
    
                        
    
    
    
                        The line 59 and 65 don't work
    
    
    
    
    
    
"""




# @pytest.fixture()
# def test_account1():
#     account = Account()
#     account.accNo = 1234
#     account.name = "hazem hashem"
#     account.type = "C"
#     account.deposit = 500
#     return account

# @pytest.fixture()
# def test_data_file(test_account1):
#     file_name = "test_accounts.data"
#     with open(file_name, "wb") as f:
#         pickle.dump([test_account1], f)
#     yield file_name
#     os.remove(file_name)


# def test_writeAccountsFile(test_account1, test_data_file):
#     with patch("builtins.input", side_effect=[1234, "hazem hashem", "C", 500]):
#         writeAccountsFile(test_account1)
#     with open("test_accounts.data", "rb") as f:
#         accounts = pickle.load(f)





# def test_displaySp(capsys, test_account1, test_data_file):
#     # call the function with input value and capture the output
#     displaySp(1234)
#     captured = capsys.readouterr()
#     # assert captured.out == "Your account Balance is =  " + str(test_account1.deposit) + "\n"
    
#     # test displayAll function 

#     displayAll()
#     captured = capsys.readouterr()
#     # assert captured.out == print(test_account1.accNo," ",test_account1.name, " ",test_account1.type," ",test_account1.deposit )



def test_displaySp_found():
    # Create a mock object for the file
    mock_file = MagicMock()
    # Mock the return value of `exists()` to True
    mock_file.exists.return_value = True

    # Create a mock object for the open function
    mock_open = MagicMock()
    # Mock the return value of `open()`
    mock_open.return_value = mock_file

    # Create a mock object for the pickle module
    mock_pickle = MagicMock()
    # Mock the return value of `load()`
    mock_pickle.load.return_value = [
        MagicMock(accNo=123, deposit=100)    ]

    # Patch the necessary functions and modules with the mocks
    with patch('builtins.print') as mock_print, \
         patch('pathlib.Path', MagicMock(return_value=mock_file)), \
         patch('builtins.open', mock_open), \
         patch('pickle.load', mock_pickle.load):
             
        # Call the function under test
        displaySp(123)

    # Assert that the expected output is printed
    mock_print.assert_called_once_with("Your account Balance is = ", 100)


def test_displaySp_not_found():
    # Create a mock object for the file
    mock_file = MagicMock()
    # Mock the return value of `exists()` to True
    mock_file.exists.return_value = True

    # Create a mock object for the open function
    mock_open = MagicMock()
    # Mock the return value of `open()`
    mock_open.return_value = mock_file

    # Create a mock object for the pickle module
    mock_pickle = MagicMock()
    # Mock the return value of `load()`
    mock_pickle.load.return_value = [
        MagicMock(accNo=123, deposit=100),
        MagicMock(accNo=456, deposit=200)
    ]

    # Patch the necessary functions and modules with the mocks
    with patch('builtins.print') as mock_print, \
         patch('pathlib.Path', MagicMock(return_value=mock_file)), \
         patch('builtins.open', mock_open), \
         patch('pickle.load', mock_pickle.load):
             
        # Call the function under test
        displaySp(789)

    # Assert that the expected output is printed
    mock_print.assert_called_once_with("No record found")
