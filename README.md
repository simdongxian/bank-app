# Bank Application
This is a python command line based bank application.
## Design
OOP is used for designing the bank account. This allows the application to be expanded in the future for multiple users and transactions between users.

Currently the Account class contains 3 private properties, balance,transactions, and amount length.

 Transactions is an array of hashmap each containing transaction date time, transaction amount and account balance. 

 Amount length is used for formatting the get_statement function which returns a table of transactions.
### Assumptions
If users enter invalid input in the menu, the menu will prompt for a valid input.

If users enter an invalid input (negative, non float) in the deposit option, the application will not process the deposit and will return to the menu.

If users enter an invalid input (negative, non float, amount more than balance) in the withdraw option, the application will not process the withdrawal and will return to the menu.

## Running the application
### Requirements:
```
python3 version 3.10.9
pytest version 7.2.2
```
### Working on:
```
MacOS 13.0.1
Windows 10
```
Open the terminal and navigate to the project directory containing app.py

Run the following command to start the application
```
python3 app.py
```
## Tests
Tests are done for the 3 main functions, withdraw, deposit and print statement.

For withdraw there are 4 test cases, sufficient balance, insufficient balance and empty string input and negative input.\
For deposit there are 3 test cases, amount > 0, amount <= 0 and invalid input.\
For print statement there are 3 test cases, no transactions, 2 valid transactions and 2 valid + 1 non valid transactions.

### Running Tests
Check if pytest is installed using the following command
```
pytest --version
```
If pytest is not installed, run the following command to install the latest version.
```
pip install -U pytest
```
In the terminal, navigate to the project directory and run the following command to run unit tests
```
pytest
```
