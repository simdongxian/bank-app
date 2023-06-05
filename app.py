from Account import Account

# Messages
menu_message = """[D]eposit
[W]ithdraw
[P]rint statement
[Q]uit
>"""

welcome_message = "Welcome to ZBank! What would you like to do?"

exit_message = """Thank you for banking with ZBank.
Have a nice day!"""

# Input handler
# Takes in input value from main and a bank account for the transaction


def handle_input(inp, account):

    # Deposit
    if inp == "d":
        inp = input("Please enter the amount to deposit: ")
        print(account.deposit(inp))
        print("Is there anything else you'd like to do?")
        return
    # Withdraw
    elif inp == "w":

        inp = input("Please enter the amount to withdraw: ")
        print(account.withdraw(inp))
        print("Is there anything else you'd like to do?")
        return
    # Print statement
    elif inp == "p":
        print(account.get_statement())
        print("Is there anything else you'd like to do?")
        return
    # Quit
    elif inp == "q":
        return
    # Invalid input
    else:
        print("Invalid input. Please try again.")


def main():
    print()
    inp = ""

    # Initialise a new account with 0 balance
    account = Account(0)

    print(welcome_message)
    # Loops program until q or Q is received
    while inp != "q":
        # convert input to lower case
        inp = input(menu_message).lower()
        print()
        handle_input(inp, account)

    print(exit_message)


main()
