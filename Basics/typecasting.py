# Typecasting: the process of converting one data type to another data type

name = ""
age = 30
gpa = 3.5
is_japanese = True

# return the data type of the variable
type(name)
print(type(name))

# if you want to see if the variable is a certain data type
# use is syntax. It returns a boolean value.
# The same idea as the typeof operator in JavaScript
print(type(name) is str)

# typecasting
# bool() function always returns True unless the value is 0, empty string, or None
# we could use this behavior to check if a variable is empty
# i.e. if someone didn't enter their name
name = bool(name)
print(name)