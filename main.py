"""
while True:
    print("1. Create")
    print("2. Update")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("Create")
    elif ch == 2:
        print("Update")
    elif ch == 3:
        print("Exit")
        break

"""

"""
a = 1.21
b = 220.44
print("Balance Expense")
print("%7.2f %7.2f" % (a, b))
"""
"""
import os
import datetime
import time

file_path = "pass.txt"

if not os.path.exists(file_path):
    file = open("pass.txt", "w")
    file.write(" Balance  Expense     Gain \t\tDate and Time \n")
    file.close()

file = open("pass.txt", "a")
file.write("%8.2f %8.2f %8.2f \t%s\n" % (100.09, 20.55, 43.4, datetime.datetime.now()))
file = open("pass.txt", "r")
print(file.read())
file.close()
"""
"""
file = open("pass.txt", "r")
obj = ""
for i in file:
    obj = i

print(obj)

obj = obj.lstrip()

num = obj.split(" ")

print(num[0])
"""
import datetime
import time


class Passbook:
    balance = 0

    def __init__(self):
        import os
        file_path = "pass.txt"

        if not os.path.exists(file_path):
            file = open("pass.txt", "w")
            file.write(" Balance  Expense     Gain \t\tDate and Time \n")
            file.close()
            balance = float(input("Enter the initial balance: "))
        else:
            file = open("pass.txt", "r")
            obj = ""
            for i in file:
                obj = i
            obj = obj.lstrip()
            num = obj.split(" ")
            balance = num[0]
            file.close()

    def withdraw(self):
        with_amount = float(input("Enter the amount: "))
        if with_amount > self.balance:
            print("Enter a valid amount")
            print("Your current balance is",self.balance)
        else:
            self.balance -= with_amount
            file = open("pass.txt", "w")
            file.write("%8.2f %8.2f %8.2f \t%s\n" % (self.balance, with_amount, 0, datetime.datetime.now()))

    def deposite(self):




book = Passbook()

while True:
    print("----------MENU----------")
    print("1. Print Balance Book")
    print("2. Register a Expense")
    print("3. Register a Gain")
    print("4. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("Create")
    elif ch == 2:
        print("Update")
    elif ch == 3:
        print("Exit")
        break
