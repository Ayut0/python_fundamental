# List[]
fruits = ["apple", "orange", "banana", "coconut"]

# fruits.append("grape")
# fruits.remove("banana")
fruits.clear()

for fruit in fruits:
    print(fruit)

# Tuple()
# immutable, faster to access than list

vegetables = ("carrot", "potato", "onion", "tomato")

# Set{}
# mutable(add/remove)
# no duplicates

milk = {"cow", "oat", "soy", "almond"}

target_milk = input("Enter the type of milk you want to find: ")

# milk.add("2%")
# milk.remove("cow")
# milk.pop()

# for m in milk:
#     print(m)

if target_milk in milk:
    print(f"{target_milk} was found")
else:
    print(f"{target_milk} was not found")

