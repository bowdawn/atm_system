
import getpass
import json
def insert_card():
    cardInserted = False
    inputCorrect= False
    while not inputCorrect: 
        user_input = input("Insert card? (yes/no): ").lower()
        if user_input == 'yes':
            print("Card inserted!")
            cardInserted = True
            inputCorrect= True
        elif user_input == 'no':
            print("No card inserted.")
            inputCorrect= True
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    return cardInserted

def enter_pin_number():
    inputCorrect= False
    attempts = 0 
    while not inputCorrect:
        if attempts >= 3: 
            print("Attempts Exceeded. Please Try Again Later. . .")
            return False
        user_input = getpass.getpass("Enter Pin Number? (****): ")
        # Check if input consists only of digits and has the desired length
        if user_input.isdigit() and len(user_input) == 4:
            validatePin = True
            if validatePin:
                print("Pin Code is Correct!")
                return True
            else: 
                attempts += 1
                print("Pin Code is Incorrect!")
        else:
            attempts += 1
            print("Invalid input. Please enter a 4-digit PIN number.")
            

def select_account():
    print("For simplicity, assume there's only one account")
    return True

def display_options():
    print("1. See Balance")
    print("2. Deposit")
    print("3. Withdraw")


def perform_transaction(option):
    try:
        with open("balance.json", 'r') as json_file:
            balance = json.load(json_file)["balance"]
    except FileNotFoundError:
        print("Error: balance.json not found. Please initialize the account.")
        return

    if option == 1:
        print(f"Account Balance: ${balance}")
    elif option == 2:
        try:
            amount = int(input("Enter deposit amount: $"))
            if amount <= 0:
                print("Error: Deposit amount must be greater than 0.")
                return
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
            return

        print("Deposit successful!")
        with open("balance.json", 'w') as json_file:
            json.dump({"balance": amount + balance}, json_file, indent=2)
    elif option == 3:
        try:
            amount = int(input("Enter withdrawal amount: $"))
            if amount <= 0 or amount > balance:
                print("Error: Invalid withdrawal amount.")
                return
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
            return

        print("Withdrawal successful!")
        with open("balance.json", 'w') as json_file:
            json.dump({"balance": balance - amount}, json_file, indent=2)
    else:
        print("Error: Invalid option. Please choose a valid option.")

def select_transactions():
 

    while True:
        display_options()
        option = int(input("Select an option (1/2/3): "))
        if option in [1, 2, 3]:
            perform_transaction( option)
        else:
            print("Invalid option. Please select 1, 2, or 3.")

        another_transaction = input("Do you want to perform another transaction? (yes/no): ").lower()
        while another_transaction not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            another_transaction = input("Do you want to perform another transaction? (yes/no): ").lower()

        if another_transaction != 'yes':
            print("Thank you for using the ATM. Goodbye!")
            break


    


def simple_atm_controller():
    continueFlow =  insert_card()
    if continueFlow:
        continueFlow = enter_pin_number()
    if continueFlow:
        continueFlow = select_account()
    if continueFlow:
        select_transactions()
        
simple_atm_controller()