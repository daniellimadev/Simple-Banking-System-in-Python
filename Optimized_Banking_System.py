import textwrap

def menu():
    menu = """\n
    ============================== MENU ============================
    [d]\tDeposit
    [s]\tWithdraw
    [e]\tExtract
    [q]\tQuit
    [nu]\tNew User
    [na]\tNew Account
    [la]\tList of accounts
    ====================================================================
    Command => """
    return input(textwrap.dedent(menu))
        
def deposit(balance, amount, statement, /):

    if amount > 0:
        balance += amount
        extract += f'Deposit:\tR$ {amount:.2f}\n'
        print('\nDeposit made successfully!')
    
    else:
        print('\nOperation failed! The amount entered is invalid.')
    
    return balance, statement

def withdrawal(*, balance, amount, statement, limit, number_withdrawals, limit_withdrawals):

    exceeded_balance = amount > balance
    exceeded_limit = amount > limit
    exceeded_withdrawals = number_withdrawals > limit_withdrawals

    if exceeded_balance:
        print("\nOperation failed! You don't have enough balance.")

    elif exceeded_limit:
        print("\nOperation failed! You don't have enough limit.")

    elif exceeded_withdrawals:
        print('\nOperation failed! Maximum number of withdrawals exceeded.')

    elif amount > 0:
        balance -= amount
        extract += f'Withdrawal:\t\tR$ {amount:.2f}\n'
        number_withdrawals += 1
        print('Withdrawal completed successfully!')

    else:
        print('\nOperation failed! The amount entered is invalid.')

    return balance, statement

def print_extract(balance, /, *, extract):
    print("============================ EXTRACT ==============================")
    print("No transactions were made on the account." if not extract else extract)
    print(f"\nBalance: R$ {balance:.2f}")
    print("=================================================================================")

def create_user(users):

    cpf = input('Enter your CPF (numbers only): ')
    user = filter_users(cpf, users)

    if user:
        print('There is already a user with this CPF: ')
        return
    
    name = input('Enter full name: ')
    date_birth = input('Enter date of birth (dd-mm-yyyy): ')
    address = input('Enter the address (street, N - neighborhood - city/state acronym)')

    users.append({'name': name, 'date_birth': date_birth, 'cpf': cpf, 'address': address})

    print('User registered successfully!')

def filter_users(cpf, users):

    filtered_users = [user for user in users if user['cpf'] == cpf]
    return filtered_users[0] if filtered_users else None

def create_account(agency, account_number, users):

    cpf = input("enter the user's CPF: ")
    user = filter_users(cpf, users)

    if user:
        print('\nAccount created successfully!')
        return {'agency': agency, 'number_account': account_number, 'user': user}

    print('\nUser not found, account creation process closed: ')
    return None


def list_accounts(accounts):
    
    for account in accounts:
        line = f"""\
            Agency:\t{account['agency']}
            C/C:\t{account['numero_conta']}
            Holder:\t{account['user']['name']}
        """
        print('=' * 100)
        print(textwrap.dedent(line))

def main():
    WITHDRAWAL_LIMIT = 3
    AGENCY = '0001'

    balance = 0
    limit = 500
    extract = ""
    number_withdrawals = 0
    users = []
    accounts = []
    
    while True:

        option = menu()

        if option == 'd':
            amount = float(input('Enter the deposit amount: '))
    
            balance, statement = deposit(balance, amount, statement)

        elif option == 's':
            amount = float(input('Enter the withdrawal amount: '))

            balance, statement = withdrawal(
                balance=balance,
                value=amount,
                extract=extract,
                limit=limit,
                number_withdrawals=number_withdrawals,
                limit_saques=WITHDRAWAL_LIMIT,
            )

        elif option == 'e':
            print_extract(balance, statement=statement)

        elif option == 'naked':
            create_user(users)

        elif option == 'na':
            account_number = len(accounts) + 1
            account = create_account(AGENCY, account_number, users)

            if account:
                account.append(account)

        elif option == 'la':
            list_accounts(accounts)

        elif option == 'q':
            break

        else:
            print('Invalid option, please select a valid option again.')

main()