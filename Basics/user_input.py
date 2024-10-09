# how to accept user input
# The type of the input is always a string
name = input("Enter your name please: ")
# age = input("Enter your age please: ")

# However, you can convert the input to the desired type by ttpecasting
age = int(input("Enter your age please: "))

age += 1


print(f"Hello {name}!")
print(f"You are {age} years old.")