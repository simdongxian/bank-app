from datetime import datetime

class Account:

    def __init__(self, balance):
        self.__balance = balance
        self.__transactions = []
        self.__amount_length = 7
    
    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            return "Please enter a valid amount."
        
        if (amount <= 0):
            return "Please enter an amount more than 0."
        
        elif (amount > self.__balance):
            return "Sorry. You have insufficient balance in your account."
        else:
            self.__balance -= amount

            transaction = {"date":get_current_time(),
                           "amount":"-"+"{:.2f}".format(amount),
                           "balance":"{:.2f}".format(self.__balance)}
            self.__transactions.append(transaction)

            if len(transaction["amount"]) > self.__amount_length:
                self.__amount_length = len(transaction["amount"])
        
            return"Thank you. ${:.2f} has been withdrawn.".format(amount)

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            return "Please enter a valid amount."
        
        if (amount <= 0):
            return "Please enter an amount more than 0."

        else:
            self.__balance += amount

            transaction = {"date":get_current_time(),
                           "amount":"{:.2f}".format(amount),
                           "balance":"{:.2f}".format(self.__balance)}
            self.__transactions.append(transaction)

            if len(transaction["amount"] ) >self.__amount_length:
                self.__amount_length = len(transaction["amount"])
            return "Thank you. ${:.2f} has been deposited to your account.".format(amount)
    
    def get_statement(self):
        if len(self.__transactions) == 0:
            return "Sorry. No transaction found."

        else:
            transactions_message = f"Date                   | {'Amount'.ljust(self.__amount_length)} | Balance\n"
            for transaction in self.__transactions:
                transactions_message += f"{transaction.get('date')} | {transaction.get('amount').ljust(self.__amount_length)} | {transaction.get('balance')}\n"
            return transactions_message
    
    def get_transactions(self):
        return self.__transactions
    
    def get_balance(self):
        return self.__balance

def get_current_time():
    return datetime.now().strftime("%d %b %Y %I:%M:%S%p")