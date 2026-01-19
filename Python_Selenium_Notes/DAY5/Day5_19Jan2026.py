#! Inheritance in python

# class Animal:
#     def speak(self):
#         print("Animal makes a sound")
        

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
        
# d=Dog()
# d.speak()
# d.bark()

#~ Mutiple Inheritance

# class A:
#     def showA(self):
#         print("A")
    
# class B:
#     def showB(self):
#         print("B")
        
# class C(A,B):
#     pass 

# c=C()
# c.showA()
# c.showB()


#! Multi level inheritance

# class A:
#     def a(self):
#         print("A")
    
# class B(A):
#     def b(self):
#         print("B")
        
# class C(B):
#     def c(self):
#         print("C")
    
# obj=C()
# obj.c()
# obj.b()
# obj.a()

#! Hierarchical Inheritance

# class Parent:
#     def parent1(self):
#         print("Parent1")
        
# class Child1(Parent):
#     def c1(self):
#         print("child1")

# class Child2(Parent):
#     def c2(self):
#         print("child2")
        
# obj1=Child1()
# obj1.c1() 
# obj1.parent1()

# obj2=Child2()
# obj2.c2()
# obj2.parent1()

