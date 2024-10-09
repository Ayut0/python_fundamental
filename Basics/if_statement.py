age =int(input("Enter your age please: "))
has_ticket = True

if age >= 18:
    print("You are an adult.")
elif age < 0:
    print("You are not born yet.")
elif age == 0:
    print("You are a new born.")
else:
    print("You are a minor.")

if has_ticket:
    print("You may enter, you have a ticket.")
else:
    print("You need to buy ticket.")