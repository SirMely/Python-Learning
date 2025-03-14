# (Python allows you to read from and write to files using build in functions)

# Writing to a File (To write to a file, use "w" mode (write mode)) This makes a file
with open("index.html", "w") as file:
    file.write("<h1>Hello, this is my first file!<h1>\n") # \n makes a new line for text
    file.write("<p>Python makes it easy.!<p>\n")

# Appending to a file (Adding content to an existing file use "a" mode (append mode))
with open("index.html", "a") as file:
    file.write("Adding a new line!")

# Reading from a File (use "r" mode aka read mode)
with open("index.html", "r") as file:
    content = file.read()
    print(content) # reads and prints everything in the file 

# Reading Line by Line
with open ("index.html", "r") as file:
    for line in file:
        print(line.strip()) # strip() removes extra spaces & new lines