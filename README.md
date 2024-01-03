# Simple Banking System in Python!! 🏦💰💰

## Technologies used

* **Language:** Python
* **Versioning:** Git/GitHub
* **IDE:** Visual Studio Code

---

### **CHALLENGE**

We were hired by a large bank to develop their new system. This bank wants to modernize its operations and for this purpose it chose the Python language. For the first version of the system we must implement only 3 operations: deposit, withdrawal and statement.

**General objective**

Create a banking system with operations:
* To withdraw
* Deposit
* View extract

---

**Operations**

* Deposit operation

It is possible to deposit positive amounts into my bank account. v1 of the project only works with 1 user, so we don't need to worry about identifying the agency number and bank account. All deposits must be stored in a variable and displayed in the statement operation.

* Withdrawal operation

The system must allow you to make 3 daily withdrawals with a maximum limit of $500.00 per withdrawal. If the user does not have a balance in their account, the system should display a message stating that it will not be possible to withdraw the money due to lack of balance. All withdrawals must be stored in a variable and displayed in the statement operation.

** Statement operation

This operation must list all deposits and withdrawals made to the account. At the end of the list, the current account balance should be displayed. If the statement is blank, display the message: No transactions were carried out.

Values ​​must be displayed using the format $ xxx.xx

*Examples*

1900.95 = $ 1900.95

---
### **CHALLENGE**

We need to make our code more modularized, to do this we will create functions for existing operations: withdrawing, depositing and viewing history. Furthermore, for version 2 of our system we need to create two new roles: user (bank customer) and create current account (link with user).

**General objective**

Separate existing withdrawal, deposit and statement functions into functions. Create two new functions: register user (customer) and register bank account.

---