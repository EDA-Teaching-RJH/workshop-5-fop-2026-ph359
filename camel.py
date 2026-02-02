# Enter your code here
camel_name = input("Enter your name in Camel Case: ")
snake_name = ""

for char in camel_name:
    if char.isupper():
        snake_name += "_" + char.lower()
    else:
        snake_name += char

print("Name in Snake: " , snake_name)


