#! Question – Class Types & Inheritance

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
