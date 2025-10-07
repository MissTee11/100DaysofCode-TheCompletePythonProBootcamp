print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_choice=input("You're at a crossroad, where do you want to go? Type 'left' or 'right'.").lower()

if first_choice=="left":
    second_choice= input("You have come to a lake. There is an island in the middle of the lake, Type 'wait' to wait for a boat. Type 'swim' to swim across").lower()

    if second_choice == "wait":
        third_choice=input("You arrive at the island unharmed. There are three doors, one is yellow, one red and one blue. Which color do you choose?").lower()

        if third_choice=="red":
            print("It's a room full of fire. Game over.")

        elif third_choice =="yellow":
            print("You found the treasure. You win!")

        elif third_choice == "blue":
            print("You room leads to the edge of a cliff. You fell off. Game Over")
        else:
            print("You were captured by cannibals. Game over.")
    else:
        print("You got attacked by a hippo. Game over.")
else:
    print("You fell into a hole. Game Over.")


