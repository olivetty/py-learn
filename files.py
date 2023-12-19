file_path = "text.txt"
text = "Sample text to save\nNew line!"
text2 = "\nThis text will be appended to the file."
#
try:
    with open(file_path, "r") as file:
        content = file.read()

    print(content)
    print(type(content))
except FileNotFoundError:
    print("File not found.")

# Write over the content to file
with open(file_path, "w") as file:
    file.write(text)

# Append to the content to file
with open(file_path, "a") as file:
    file.write(text2)