# Try-Except-Else
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}") # Only runs if no exception is raised
