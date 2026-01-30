#takes function as parameter and returns fuction as parameter but with some modifications that you want to do. 

# def log_deco(func):
#     def wrap(*args,**kwargs):
#         print("values",args)
#         result=func(*args)
#         print(result)
#         return result
#     return wrap

# def greater_first(func):
#     def wrap(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return wrap

# @log_deco
# @greater_first
# def sub(a,b):
#     return a-b

# @log_deco
# @greater_first
# def divide(a,b):
#     return a/b 


# print(divide(2,4))
# print(sub(10,4))


def logger(func):
    def wrap(**args):
        print("before function")
        func()
        print("after function")
    return wrap

@logger
def greet():
    print("Hello Python!")

greet()