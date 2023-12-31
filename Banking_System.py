menu = """
============================== MENU =============================
                        [d] - Deposit
                        [s] - Withdraw
                        [e] - Extract
                        [q] - Exit
====================================================================
"""

balance = 0
limit = 500
extract = ""
number_withdrawals = 0
WITHDRAWAL_LIMIT = 3

while True:
    option = input(menu)

    if option == "d":
        value = float(input("Enter the amount to be deposited: "))

        if value > 0:
            print(f"Deposit made successfully! $ {value:.2f}\n")
            balance += value
            extract += f"Deposit made: {value:.2f}\n"

        else:
            print("Operation failed: The value entered is invalid")
    
    elif option == "s":

        value = float(input("Enter the withdrawal value: "))

        exceeded_balance = value > limit
        exceeded_limit = value > limit
        exceeded_withdrawals = number_withdrawals >= WITHDRAWAL_LIMIT

        if exceeded_balance:
            print("Operation failed! You do not have enough balance.")

        elif exceeded_limit:
            print("Operation failed! The withdrawal amount exceeds the limit.")

        elif exceeded_withdrawals:
            print("Operation failed! The maximum number of withdrawals reached.")

        elif value > 0:
            print(f"Withdrawal completed successfully! $ {value:.2f}\n")
            balance -= value
            extract += f"Withdrawal made: {value:.2f}\n"

        else:
            print("Operation failed: The value entered is invalid.")

    elif option == "e":
        print("============================ EXTRACT ==============================")
        print("No transactions were made on the account." if not extract else extract)
        print(f"\nBalance: $ {balance:.2f}")
        print("=================================================================================")

    elif option == "q":
        break
    
    else:
        print("Invalid operation, please select a valid command.")