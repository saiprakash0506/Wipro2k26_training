a=10                               #global variable

def something():

    globals()["a"]=20

    a=15                               #local variable
    print("inside",a)

something()

print("outside",a)