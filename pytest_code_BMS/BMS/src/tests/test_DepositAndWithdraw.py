import pytest
import os.path
import pickle
from BMS.src.DepositAndWithdraw import Account, depositAndWithdraw


@pytest.fixture()
def test_account():
    account = Account()
    account.accNo = 1234
    account.name = "hazem hashem"
    account.type = "C"
    account.deposit = 500
    return account


@pytest.fixture()
def test_data_file(test_account):
    file_name = "test_accounts.data"
    with open(file_name, "wb") as f:
        pickle.dump([test_account], f)
    yield file_name
    os.remove(file_name)


def test_deposit_and_withdraw(test_account, test_data_file, capsys):
    # deposit test
    with open("test_accounts.data", "rb") as f:
        accounts = pickle.load(f)
    assert len(accounts) == 1
    assert accounts[0].deposit == 500

    depositAndWithdraw(1234, 1)  # deposit 1
    with open("test_accounts.data", "rb") as f:
        accounts = pickle.load(f)
    assert accounts[0].deposit == 500

    # withdraw test
    depositAndWithdraw(1234, 2)  # withdraw 1
    with open("test_accounts.data", "rb") as f:
        accounts = pickle.load(f)
    assert accounts[0].deposit >= 440

    def test_no_records_found(capsys):
        # test account not found
        depositAndWithdraw(5678, 1)  # deposit 1
        captured = capsys.readouterr()
        assert captured.out == "No records to search\n"