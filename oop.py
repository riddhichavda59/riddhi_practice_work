# Python OOP Examples

# Class definition

# A class is a blueprint or template used to create objects.
# It defined what data and actions an object will have.
# Data : Attributed
# Actions : Methods

# House Bluperint

# Class = Blueprint / Design

# Object defination

# An object is a real instance of a class.

# It contains actual values and can use the methods defined in the class.

# Blueprint -> Honda , Audi, Tesla

# Object : Real thing

# Encapsulations

# Encpsulation means keeping data and methods together inside a class and protecting important data from direct access.

# ATM Machine -> Withdraw Cash -> Deposit Case

# Encapsulation = Data Protection +  Controlled Access
'''
class ClassName:
  pass

car = className()
'''
'''
1. Attributes
2. Constructor
3. Destructor
4. self keyword
'''

class Car:

  # contsructor

  def __init__(self , brand=None , model=None , color=None , price=None , name=None , age=None , dob=None , marks=None):

    # car
    self.brand = brand
    self.model = model
    self.color = color
    self.price = price

    #user
    self.name = name
    self.age = age
    self.dob = dob
    self.marks = marks
   

  # Method

  def start(self):
    print(f"{self.brand} {self.model} is Starting.....")

  # Method

  def Car_Details(self):
    print(f"""
    Brand : {self.brand}
    Model : {self.model}
    Color : {self.color}
    Price : {self.price}
    """)

  def User_Details(self):
    print(f"""
    Name : {self.name}
    Age : {self.age}
    DOB : {self.dob}
    Marks : {self.marks}
    """)

car1 = Car("Honda" , "Amaze" , "Black" , "10000" , "vivek" , 25 , "01-01-2000" , 85)

car1.Car_Details()


class Student:

  # contsructor

  def __init__(self , name , age , dob , marks):

    #user
    self.name = name
    self.age = age
    self.dob = dob
    self.marks = marks
   
  def User_Details(self):
    print(f"""
    Name : {self.name}
    Age : {self.age}
    DOB : {self.dob}
    Marks : {self.marks}
    """)

student1 = Student("Vivek" , 25 , "01-01-2000" , 85)

student1.User_Details()


# Simple Creation

class Person:
  pass

p1 = Person()

print(type(p1))


class Person:

  name = "Vivek"

  age = 25

  course = "Python"

p1 = Person()

print(p1.name)
print(p1.age)
print(p1.course)


# Class with Method and Constructor

class Student:

  def __init__(self):
    self.name = "vivek"
    self.age = 20

  def display(self):
    print(f"Welcome to Python OOP")

s1 = Student()

s1.display()
s1.name = "Rahul"
print(s1.name)
print(s1.age)

# Bank Account App

class BankAccount:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def __init__(self,amount):
        self.balance += amount
        print("Amount Deposite Successfully!.")

    def __init__(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdraw successfully!")
        else:
            print("Account balance is low.")

    def check_balance(self):
        print("Account Balance:",self.balance)

account = BankAccount("vivek",100)
account.balance = 1000000000000

#name = input("Enter Account holder name : ")
#balance = float(input("Enter Opening Balance:"))

#account = BankAccount(name , balance)

while True:

  print("1. Deposit")
  print("2. Withdraw")
  print("3. Check Balance")
  print("4. Exit")

  choice = int(input("Enter your choice : "))

  if choice == 1:

    amount = float(input("Enter deposite amount : "))
    account.deposite(amount)

  elif choice == 2:

    amount = float(input("Enter withdraw amount : "))
    account.withdraw(amount)

  elif choice == 3:
    account.check_balance()

  elif choice == 4:
    print("Thank You!!!!")
    break

  else:
    print("Invalid Choice")


       
        

        
