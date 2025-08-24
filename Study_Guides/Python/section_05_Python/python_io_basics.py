# Python I/O Basics

# --- User Input ---

# input() reads a line from user input (as a string)
name = input("Enter your name: ")
print("Hello,", name)  # Prints greeting with the name

# You can cast input to other types
age = int(input("Enter your age: "))  # Converts the input to an integer
print("In 5 years, you'll be", age + 5)

# --- Output with print() ---

# print() outputs data to the console
print("This is a line of text.")

# You can print multiple values, separated by commas
print("Sum of 3 and 4 is", 3 + 4)

# Customize separator and end character
print("A", "B", "C", sep="-", end="\nEND\n")  # Outputs: A-B-C followed by END on a new line

# --- File I/O ---

# The built-in open() function is used to open a file.
# It returns a file object, which you can use to read from or write to the file.
# Syntax: open(filename, mode)
# Modes include:
#   'r' - read (default)
#   'w' - write (creates or overwrites)
#   'a' - append (adds to end)
#   'b' - binary mode (e.g., 'rb', 'wb')

# Writing to a file
with open("example.txt", "w") as file:  # Opens file for writing
    file.write("Hello, file!\n")
    file.write("This is the second line.\n")

# Reading from a file
with open("example.txt", "r") as file:  # Opens file for reading
    content = file.read()  # Reads entire content into a string
    print("File content:")
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())  # .strip() removes trailing newline characters

# Appending to a file
with open("example.txt", "a") as file:  # Opens file for appending
    file.write("Appending a new line.\n")
