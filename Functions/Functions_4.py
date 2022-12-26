# Variable length arguments - *args
def add(*x):
    # convert x variable into a tuple
    sum = 0
    for num in x:
        sum += num 
    print("Sum is",sum)

add(3,4)
add(5)
add()
add(4,6,3,6)
add(5,3,6,8,9,4,2)

# Keyword variable length - **kwargs
# **kwargs = keyword arguments

def person(**details):
    # convert details variable into a dictionary
    print(details)

person(name="John")
person(id=101, name="Sam", salary=45000)
person(id=102, name="Max", phone=987653368, address="delhi")


def show(**n):
    print(n)

show(x1=12, x2=15, x3=18)
show(a=12, b=15)
show(x=12, y=15, z=18)
