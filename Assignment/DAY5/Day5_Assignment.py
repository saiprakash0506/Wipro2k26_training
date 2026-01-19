#! Question – Class Types & Inheritance

#~ Topics: Class types, Introduction to Inheritance, Types of Inheritance

#* Question 1

'''1. Create a base class Vehicle with a method start()			
			
2. Create a derived class Car that inherits from Vehicle			
			
3. Add a class variable to track the number of vehicles created			
			
4. Demonstrate single inheritance and multilevel inheritance with appropriate classes			
'''

class Vehicle:
    Vehicle_count=0
    
    def __init__(self):
        Vehicle.Vehicle_count+=1 
        
    def start(self):
        print("Vehicle started")
        
#single Inheritance

class Car(Vehicle):
    def drive(self):
        print("car is driving")
        
#Multi level inheritance

class Evcar(Car):
    def charge(self):
        print("Electric car is charging")
        
v=Vehicle()
c=Car()
e=Evcar()

v.start()
c.start()
c.drive()

e.start()
e.drive()
e.charge()

#! Question – Parameterized Methods, Constructors & Destructors

#~ Topics: Parameterized Methods, Constructors & Destructors

'''Create a class BankAccount that:		
		
1. Uses a parameterized constructor to initialize account_number and balance		
		
2. Implements methods deposit(amount) and withdraw(amount)		
		
3. Uses a destructor to display a message when the object is deleted		
		
4. Handle invalid withdrawal using proper checks		
'''

class BankAccount:

    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        self.amount=amount
        self.balance=self.amount+self.balance
        print(self.amount ,"RS deposited successfully")
        print("Total balance is :",self.balance,"RS")

    def withdrawn(self,amount):
        self.amount=amount
        if self.balance>=self.amount:
            self.balance=self.balance-self.amount
            print(self.amount,"RS withdrawn successfully")
            print("Total balance is :",self.balance,"RS")
        else:
            print("oops sorry!! Insuffient funds")

b=BankAccount(123,1000)
b.deposit(1000000000)
b.withdrawn(20000)