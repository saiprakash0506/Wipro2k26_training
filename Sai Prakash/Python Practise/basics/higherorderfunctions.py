
#a function which takes another function has input is known as higher order functions

def square(num):
    return num*num 

def cube(num):
    return num*num*num 

def operate(num,operation): #accepting another function
    for i in nums:
        result=operation(i)
        print(result)

nums=[5,6,7,8,9]
operate(nums,square)
