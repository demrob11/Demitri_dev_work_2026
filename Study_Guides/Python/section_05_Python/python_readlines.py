# Python readlines() Explained

# The readlines() method reads all lines from a file and returns them as a list of strings.
# Each element in the list represents one line, including the newline character at the end.

# --- Example: Reading lines from a file ---

with open("example.txt", "r") as file:
    lines = file.readlines()  # Reads entire file into a list of lines

# Print raw lines (including newline characters)
print("Raw lines:", lines)

# You can strip newline characters with a list comprehension
cleaned_lines = [line.strip() for line in lines]
print("Cleaned lines:", cleaned_lines)

# --- Notes ---
# - Good for small to medium-sized files where you want to process all lines at once.
# - For very large files, consider reading line-by-line with a loop to save memory:

with open("example.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())

# readlines() can also take a size hint:
# It attempts to read roughly that number of bytes, stopping once that threshold is reached.

with open("example.txt", "r") as file:
    partial_lines = file.readlines(50)  # Reads ~50 bytes worth of lines
    print("Partial readlines:", partial_lines)
