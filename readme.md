# Simple ATM Controller

## Overview

This Python script represents a basic ATM controller. Users can simulate the insertion of a card, enter a PIN number, and perform simple banking transactions such as checking the balance, depositing, and withdrawing money.

## Instructions

1. **Insert Card:**

   - Run the script and respond to the prompt to insert a card by entering 'yes' or 'no'.
   - If 'yes' is chosen, the script proceeds to the next step; otherwise, it exits.

2. **Enter PIN Number:**

   - Users are prompted to enter a 4-digit PIN number.
   - After three incorrect attempts, the program locks the user out.
   - If the correct PIN is entered, the script moves to the next step.

3. **Select Account:**

   - For simplicity, the script assumes there is only one account.

4. **Perform Transactions:**

   - Users can choose from the following options:
     1. See Balance
     2. Deposit
     3. Withdraw
   - The script reads and updates the account balance stored in `balance.json`.
   - Invalid options or inputs are handled gracefully.

5. **Exit:**
   - Users can perform multiple transactions until they choose to exit by entering 'no' when prompted.

## Dependencies

- The script uses the `getpass` module for securely entering PIN numbers.
- The account balance is stored in a JSON file named `balance.json`.

## Usage

1. Run the script using a Python interpreter. Run the script using a Python interpreter.

In the repository directory run the following line of code
python atm_system.py

2. Follow the on-screen prompts to simulate the ATM interaction.
