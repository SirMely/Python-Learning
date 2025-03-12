# Basic Function (Defining a Function)

def greet():
    print("Hello, welcome to Python!")
greet() # Calls the function kinda like print()

# Functions with Parameters
def greet(name):
    print("Hello,", name)

greet("Deontae")

# Return Values

def add(a, b):
    return a + b

result = add(5,3)
print(result)
    
# Default Parameter values
def greet(name="Guest"):
    print("Hello", name)
greet()
greet("Mr.Wills")

