
temp = -36
is_raining = False

# or operator
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled.")
# else:
#     print("The outdoor event is still on.")

# and operator
if temp >= 28 and is_raining:
    print("It is too hot dude \U0001F613")
elif temp <= 0 and not is_raining:
    print("It is too cold dude \U0001F976")