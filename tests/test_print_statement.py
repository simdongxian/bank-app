from ..Account import Account

def test_print_statement():
    account = Account(20)
    account.deposit(100)
    account.withdraw(30)
    assert account.get_balance() == 90
    transactions = account.get_transactions()
    assert len(transactions) == 2
    assert transactions[0]["amount"] == "100.00"
    assert transactions[1]["amount"] == "-30.00"

def test_print_statement_with_fails():
    account = Account(20)
    account.deposit(100)
    account.withdraw(30)
    account.withdraw(1000)
    assert account.get_balance() == 90
    transactions = account.get_transactions()
    assert len(transactions) == 2
    assert transactions[0]["amount"] == "100.00"
    assert transactions[1]["amount"] == "-30.00"


def test_print_empty():
    account = Account(0)
    assert account.get_statement() == "Sorry. No transaction found."
    assert len(account.get_transactions()) == 0