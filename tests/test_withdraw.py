from ..Account import Account

def test_withdraw_sufficient():
    account = Account(100)
    assert account.withdraw(10) == "Thank you. $10.00 has been withdrawn."
    assert account.get_balance() == 90

def test_withdraw_insufficient():
    account = Account(0)
    assert account.withdraw(50) == "Sorry. You have insufficient balance in your account."
    assert account.get_balance() == 0

def test_withdraw_emptystring():
    account = Account(50)
    assert account.withdraw("") == "Please enter a valid amount."
    assert account.get_balance() == 50

def test_withdraw_negative():
    account = Account(50)
    assert account.withdraw(-10) == "Please enter an amount more than 0."
    assert account.get_balance() == 50
        