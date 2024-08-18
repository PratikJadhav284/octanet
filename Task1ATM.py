# ATM Machine Simulation

# Account data (Sample accounts)
accounts = {
    "1234": {"balance": 1000, "history": [], "pin": "1111"},
    "5678": {"balance": 500, "history": [], "pin": "2222"},
}

def display_menu():
    print("""
    1. Account Balance Inquiry
    2. Cash Withdrawal
    3. Cash Deposit
    4. Change PIN
    5. Transaction History
    6. Exit
    """)

def atm_simulation():
    print("Welcome to the ATM!")

    # Login
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    # Validate user
    if account_number not in accounts:
        print("Invalid account number.")
        return
    elif accounts[account_number]["pin"] != pin:
        print("Invalid PIN.")
        return

    # Main menu
    while True:
        display_menu()
        option = input("Select an option: ")

        # Process option
        if option == "1":
            print(f"Your account balance is: ${accounts[account_number]['balance']}")
        
        elif option == "2":
            amount = int(input("Enter withdrawal amount: "))
            if amount > accounts[account_number]["balance"]:
                print("Insufficient funds.")
            else:
                accounts[account_number]["balance"] -= amount
                accounts[account_number]["history"].append(f"-${amount} withdrawal")
                print(f"Withdrawal successful. New balance: ${accounts[account_number]['balance']}")
        
        elif option == "3":
            amount = int(input("Enter deposit amount: "))
            accounts[account_number]["balance"] += amount
            accounts[account_number]["history"].append(f"+${amount} deposit")
            print(f"Deposit successful. New balance: ${accounts[account_number]['balance']}")
        
        elif option == "4":
            old_pin = input("Enter your old PIN: ")
            if old_pin != accounts[account_number]["pin"]:
                print("Incorrect old PIN.")
            else:
                new_pin = input("Enter your new PIN: ")
                accounts[account_number]["pin"] = new_pin
                print("PIN change successful.")
        
        elif option == "5":
            if accounts[account_number]["history"]:
                print("Transaction History:")
                for transaction in accounts[account_number]["history"]:
                    print(transaction)
            else:
                print("No transaction history available.")
        
        elif option == "6":
            print("Thank you for using the ATM!")
            break
        
        else:
            print("Invalid option. Please try again.")

# Run the ATM simulation
atm_simulation()
