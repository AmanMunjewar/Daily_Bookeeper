import datetime


def print_pass():
    file = open("pass.txt", "r")
    print(file.read())
    file.close()


class Passbook:
    balance = 0

    def __init__(self):
        import os
        file_path = "pass.txt"

        if not os.path.exists(file_path):
            file = open("pass.txt", "w")
            file.write(" Balance  Expense     Gain \t\tDate and Time \n")
            file.close()
            self.balance = float(input("Enter the initial balance: "))
        else:
            file = open("pass.txt", "r")
            obj = ""
            for i in file:
                obj = i
            obj = obj.lstrip()
            num = obj.split(" ")
            self.balance = float(num[0])
            file.close()

    def withdraw(self):
        with_amount = float(input("Enter the amount: "))
        if with_amount > self.balance:
            print("Enter a valid amount")
            print("Your current balance is", self.balance)
        else:
            self.balance -= with_amount
            file = open("pass.txt", "a")
            file.write("%8.2f %8.2f %8.2f \t%s\n" % (self.balance, with_amount, 0, datetime.datetime.now()))
            file.close()

    def deposit(self):
        depo_amount = float(input("Enter the amount: "))
        self.balance += depo_amount
        file = open("pass.txt", "a")
        file.write("%8.2f %8.2f %8.2f \t%s\n" % (self.balance, 0, depo_amount, datetime.datetime.now()))
        file.close()


print("Welcome to your own bookkeeper")
book = Passbook()

while True:
    print("\n----------MENU----------")
    print("1. Print Balance Book")
    print("2. Register a Expense")
    print("3. Register a Gain")
    print("4. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        print_pass()
    elif ch == 2:
        book.withdraw()
    elif ch == 3:
        book.deposit()
    elif ch == 4:
        print("Exit....")
        break
