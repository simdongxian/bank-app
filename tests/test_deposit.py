from ..Account import Account

def test_deposit():
    account = Account(40)
    assert account.deposit(10) == "Thank you. $10.00 has been deposited to your account."
    assert account.get_balance() == 50

def test_deposit_negative():
    account = Account(40)
    assert account.deposit(-10) == "Please enter an amount more than 0."
    assert account.get_balance() == 40

def test_deposit_invalid():
    account = Account(20)
    assert account.deposit("") == "Please enter a valid amount."
    assert account.get_balance() == 20
        