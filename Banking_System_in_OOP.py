import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def carry_out_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)


class Person(Client):
    def __init__(self, name, birth_date, cpf, address):
        super().__init__(address)
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf


class Account:
    def __init__(self, number, client):
        self._balance = 0
        self._number = number
        self.agency = "0001"
        self._client = client
        self._historic = History()

    @classmethod
    def new_account(cls, client, number):
        return cls(number, client)

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def agency(self):
        return self.agency

    @property
    def client(self):
        return self._client

    @property
    def history(self):
        return self._history

    def withdraw(self, value):
        balance = self.balance
        exceeded_balance = value > balance

        if exceeded_balance:
            print("\n@@@ Operation failed! You don't have enough balance. @@@")

        elif value > 0:
            self._balance -= value
            print("\n=== Withdrawal completed successfully! ===")
            return True

        else:
            print("\n@@@ Operation failed! The value entered is invalid. @@@")

        return False

    def deposit(self, value):
        if value > 0:
            self._balance += value
            print("\n=== Deposit made successfully! ===")
        else:
            print("\n@@@ Operation failed! The value entered is invalid. @@@")
            return False

        return True


class Current_Account(Account):
    def __init__(self, number, client, limit=500, withdrawal_limit=3):
        super().__init__(number, client)
        self.limit = limit
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, value):
        number_withdrawals = len(
            [transaction for transaction in self.history.transactions if transaction["tipo"] == Withdrawal.__name__]
        )

        exceeded_limit = value > self.limit
        exceeded_withdrawals = number_withdrawals >= self.withdrawal_limit

        if exceeded_limit:
            print("\n@@@ Operation failed! Withdrawal amount exceeds limit. @@@")

        elif exceeded_withdrawals:
            print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")

        else:
            return super().withdraw(value)

        return False

    def __str__(self):
        return f"""\
            Agency:\t{self.agency}
            C/C:\t\t{self.number}
            Holder:\t{self.client.name}
        """


class History:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "value": transaction.value,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transaction(ABC):
    @property
    @abstractproperty
    def value(self):
        pass

    @abstractclassmethod
    def register(self, account):
        pass


class Withdrawal(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        transaction_success = account.withdraw(self.value)

        if transaction_success:
            account.history.add_transaction(self)


class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        transaction_success = account.deposit(self.value)

        if transaction_success:
            account.history.add_transaction(self)
            
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDeposit
    [s]\tWithdraw
    [e]\tExtract
    [nc]\tNew account
    [lc]\tList accounts
    [nude]\tNew user
    [q]\tQuit
    => """
    return input(textwrap.dedent(menu))


def filter_client(cpf, customers):
    filtered_customers = [client for client in customers if client.cpf == cpf]
    return filtered_customers[0] if filtered_customers else None


def recover_client_account(customers):
    if not customers.accounts:
        print("\n@@@ Customer does not have an account! @@@")
        return

    # FIXME: does not allow the customer to choose the account
    return customers.accounts[0]


def deposit(customers):
    cpf = input("Enter the customer's CPF: ")
    client = filter_client(cpf, customers)

    if not client:
        print("\n@@@ Customer not found! @@@")
        return

    value = float(input("Enter the deposit amount: "))
    transaction = Deposit(value)

    account = recover_client_account(client)
    if not account:
        return

    client.carry_out_transaction(account, transaction)


def withdraw(customers):
    cpf = input("Enter the customer CPF: ")
    client = filter_client(cpf, customers)

    if not client:
        print("\n@@@ Customer not found! @@@")
        return

    value = float(input("Enter the withdrawal value: "))
    transaction = Withdrawal(value)

    account = recover_client_account(client)
    if not account:
        return

    client.carry_out_transaction(account, transaction)


def display_extract(customers):
    cpf = input("Enter the client's CPF: ")
    client = filter_client(cpf, customers)

    if not client:
        print("\n@@@ Customer not found! @@@")
        return

    account = recover_client_account(customers)
    if not account:
        return

    print("\n================ EXTRACT ================")
    transactions = account.history.transactions

    extract = ""
    if not transactions:
        extract = "No movements were carried out."
    else:
        for transaction in transactions:
            extract += f"\n{transaction['type']}:\n\t$ {transaction['value']:.2f}"

    print(extract)
    print(f"\nBalance:\n\t$ {account.balance:.2f}")
    print("=========================================")


def create_customer(customers):
    cpf = input("Enter CPF (number only): ")
    client = filter_client(cpf, customers)

    if client:
        print("\n@@@ There is already a customer with this CPF! @@@")
        return

    name = input("Enter full name: ")
    date_birth = input("Enter date of birth (dd-mm-yyyy): ")
    address = input("Enter the address (street, number - neighborhood - city/state acronym): ")

    client = Person(name=name, date_birth=date_birth, cpf=cpf, address=address)

    customers.append(client)

    print("\n=== Customer created successfully! ===")


def create_account(account_number, customers, accounts):
    cpf = input("Enter the customer's CPF: ")
    client = filter_client(cpf, customers)

    if not client:
        print("\n@@@ Customer not found, account creation flow closed! @@@")
        return

    account = Current_Account.new_account(client=client, number=account_number)
    accounts.append(account)
    client.contas.append(account)

    print("\n=== Account created successfully! ===")


def list_accounts(accounts):
    for account in accounts:
        print("=" * 100)
        print(textwrap.dedent(str(account)))


def main():
    customers = []
    accounts = []

    while True:
        option = menu()

        if option == "d":
            deposit(customers)

        elif option == "s":
            withdraw (customers)

        elif option == "e":
            display_extract(customers)

        elif option == "naked":
            create_customer(customers)

        elif option == "nc":
            account_number = len(accounts) + 1
            create_account(account_number, customers, accounts)

        elif option == "lc":
            list_accounts(accounts)

        elif option == "q":
            break

        else:
            print("\n@@@ Invalid operation, please select the desired operation again. @@@")


main()