# String Indexing & Slicing
word = "Python"
print(word[0]) # prints the first word
print(word[-1]) # prints the last word

# Slicing
print(word[0:4]) # Pyth prints characters 0 to 3
print(word[:3]) # Pyt prints 0 to 2
print(word[2:]) # thon from 2 to the end

# Common String Methods
text = "Hello, World!"

print(text.upper())  # HELLO WORLD
print(text.lower())  # hello world
print(text.title())  # Hello World
print(text.replace("Hello", "Hi"))  # Hi world
print(text.split())  # ['hello', 'world'] (Splits by space)

# String Formatting
name = "DJ"
age = 18

print(f"My name is {name} and I am {age} years old.") # the F or f"" allows us to insert variables
# Another Way
print("My name is {} and I am {} years old".format(name, age)) # Just a longer way to do it

