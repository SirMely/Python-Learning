# Lists

fruits = ["apple", "banana", "cherry"]
print(fruits[0]) # quite litterally an array lol but prints blue

fruits.append("orange") # Adds to the list/array
fruits.remove("banana")
print(fruits)

# Tuples (Like list but you cannot modify them)
colors = ("red", "green", "blue")
print(colors[1]) # obviously prints green

#Sets (Stores Unique values and they are unordered)
numbers = {1, 2, 3, 4, 4, 2} # it removes duplicates
print(numbers)

numbers.add(5) # this is how you add to sets
numbers.remove(3) # this is how you remove from sets
print(numbers)

# Dictionaries (it pairs a unique value with a specific value like Buyer Name -> Order)
person = {"name": "DJ", "age": 18, "city": "Kansas City"}
print(person["name"])

person["age"] = 19 # Change a value
person["job"] = "Software Developer" # Adds new key-value pair
print(person)