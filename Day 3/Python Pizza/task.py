print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    if pepperoni=="Y":
        if extra_cheese=="Y":
            print("Your final bill is: $18.")
        else:
            print("Your final bill is: $17.")
    else:
        if extra_cheese=="Y":
            print("Your final bill is: $16.")
        else:
            print("Your final bill is: $15.")
elif size == "M":
    if pepperoni == "Y":
        if extra_cheese == "Y":
            print("Your final bill is: $24.")
        else:
            print("Your final bill is: $23.")
    else:
        if extra_cheese == "Y":
            print("Your final bill is: $21.")
        else:
            print("Your final bill is: $20.")
else:
    if pepperoni == "Y":
        if extra_cheese == "Y":
            print("Your final bill is: $29.")
        else:
            print("Your final bill is: $28.")
    else:
        if extra_cheese == "Y":
            print("Your final bill is: $26.")
        else:
            print("Your final bill is: $25.")

# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
#
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}")
#
