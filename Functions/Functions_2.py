# Global Scope - scope of variables is for complete script
x = 23
y = 8

def addition():
    # Local Scope - scope of variables is restricted to the function only
    global x
    x = 12
    y = 21
    z = x + y
    print("Sum is",z)

def subtraction():
    z = x - y
    print("Sub is",z)

addition()
subtraction()
