# def calc(x, y):
#     z = x + y
#     # print("Sum is",z)
#     return z

# def calc(x:int, y:int) -> int:
#     z = x + y
#     return z

def calc(x:int, y:int) -> int:
    z1 = x + y
    z2 = x - y
    z3 = x / y
    z4 = x * y
    # Packing
    return z1, z2, z3, z4

# sum = calc(5,8)
# print(sum)

# Unpacking
# a,b,c,d = calc(5,8)
a,b,*c = calc(5,8)
print("Sum is",a)
print("Sub is",b)
print("Result is",c)
