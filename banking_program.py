
# Banking Program

import time

def show_balance(balance):
    print(f"Balance is ${balance:.2f}")

def deposit():
    deposit_money = float(input("Add money: $"))
    
    if deposit_money <= 0:
        print("Please enter valid amount")
        return 0
    else:
        return deposit_money

def withdraw(balance):
    withdraw_money = float(input("Withdraw money: $"))
    if withdraw_money <= 0:
        print("Please enter valid amount")
        return 0
    elif withdraw_money > balance:
        print("Insufficient funds")
        return 0
    else:
        return withdraw_money

def main():
    balance = 0
    is_running = True

    while is_running:
        print("----------")
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exist")

        choice = int(input("What do you want? "))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running = False
        else:
            print("Enter valid option. ")
        time.sleep(1)


    print("have a nice day!")  

if __name__ == '__main__':
    main()
