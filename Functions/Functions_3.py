# positional arguments - all the arguments are required
# def greet(fname, lname):
#     name = fname + " " + lname
#     print("Hello", name)

# Default argument
def greet(fname, lname=""):
    name = fname + " " + lname
    print("Hello", name)

# greet()
# greet("John")
greet("Rohit", "Sharma")

# keyword argument
greet(fname="Virat", lname="Kohli")
greet(lname="Dhoni", fname="MS")
greet("John")
