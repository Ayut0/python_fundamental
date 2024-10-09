name = input("What is your name? ")

while name == "":
    name = input("Please enter your name: ")

age = int(input("Enter your age: "))

while age < 0:
    print("Age cant be less than 0")
    age = int(input("Please Enter your age: "))

print(f"Hello, {name}!")
print(f"You are {age} years old.")