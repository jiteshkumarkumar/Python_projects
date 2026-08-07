print("======================================")
print("Welcome to ABC Bank Money Transaction!")
print("======================================")

"""
ABC Bank Money Transaction System
---------------------------------
A simple CLI program demonstrating input validation, 
exception handling, and basic banking logic in Python.
"""

balance = 0.0

'''Create the function to check all th Transaction. '''


def check_balance():
    print(f"Available Balance:{balance}")


def deposit_amount(amount):
    global balance
    if amount > 0:
        balance = balance + amount
    elif amount <= 0:
        print("Zero or Negetive can not be deposited.")
    else:
        print("Invalid Inputs")


def withdraw_amount(amount):
    global balance
    if amount > balance:
        print("Insuffient balance")
    elif balance > amount:
        balance = balance - amount
    elif balance == 0:
        print("Zero amount can not be withdrawn.")
    else:
        print("Invalid Inputs.")


print("=====================")
print("Select option 1 to 4")
print("=====================")
print()
print("Press 1. Check Balance")
print("Press 2. Deposit Amount")
print("Press 3. Withdraw Amount")
print("Press 4. Quit")

if __name__ == "__main__":
    while True:
        while True:
            try:
                choose = int(input("\nSelect option 1 to 4: "))
                break
            except ValueError:
                print("Please enter value numberic value.")

        if choose == 1:
            check_balance()
        elif choose == 2:
            while True:
                try:
                    amount = int(input("Enter deposit amount: "))

                    break
                except ValueError:
                    print("Please enter numberic value to deposit amount.")
            deposit_amount(amount)
            print("The amount has been successfully deposit ")
        elif choose == 3:
            while True:
                try:
                    amount = int(input("Enter withdraw amount: "))

                    break
                except ValueError:
                    print("Please enter numberic value to deposit amount.")
            withdraw_amount(amount)
            print("The amount has been successfully withdrawn.")
        elif choose == 4:
            print("Quiting.")
            break
        else:
            print("Please select option between 1 to 4 options.")

print("Thank you for choosing ABC Bank Money Transaction")
print("Have great day ahead.")            















