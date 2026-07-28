# Class,Object and constructor

# class User:
#     def __init__(self,name):
#         self.name = name

# u1=User("Naveen")
# print(u1.name)
# u2=User("Amit")
# print(u2.name)



# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("Name is:",self.name,"Age is:",self.age)

# u1=User("Naveen",23)
# u1.display()
# u2=User("Amit",24)
# u2.display()

# class Car:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def details(self):
#             print("Brand is:", self.brand, "Price is:", self.price)


# car1=Car("BMW", 500000)
# car1.details()
# car2=Car("RR",20000000)
# car2.details()


class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print("Deposit successful",amount)
        print("New balance",self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Withdrawal successful", amount)
            print("New balance", self.balance)
    

account1=BankAccount("Ali", 1000)

account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1300)

account2=BankAccount("Sahbaz", 2000)

account2.deposit(500)
account2.withdraw(200)
account2.withdraw(1300)

