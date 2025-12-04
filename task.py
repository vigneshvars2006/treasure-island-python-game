print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to the Treasure island!\nYour mission is to find the treasure.")

choice1 = input('''You are in the middle of the Road with two paths, one will kill you instantly
                   Because there is a monster in that path and the other path is safe, thus leading you
                   closer to the TREASURE!, It's time to make the decision, Are you going to go in
                   the left path or the right one? Choose (right) or (left)?\n ''').lower()

if choice1 == "left":
    choice2 = input('''Woah! you survived, that's good, Now there's a boat on it's way to pick you up and 
                       help you cross the river, are you going to wait for the boat or swim across the river
                       What are you going to choose now (wait) for the boat or (swim) across?\n''').lower()
    if choice2 == "wait":
        print("Now you have safely crossed across the river with the help of the boat")

        choice3 = input('''Congrats you have made it to the last mission!
                           Now you have three doors in front of you, Only one of them is safe and would take you to the tressure,
                           The rest of the two doors would kill you instantly, So tressure hunter choose wisely, There's a red door,
                           yellow door and a blue one, which color are you going to choose?\n''').lower()
        if choice3 == "yellow":
            print("Congratulations,You opened the tressure door,YOU HAVE WON THE TREASURE! YOU WON! ")
        elif choice3 == "red":
            print("Oops,You opened the door of flame,You died,Game Over.")
        elif choice3 == "blue":
            print("Oops,You opened the door of water with crocodiles,You died,Game Over.")
        else:
            print("You didn't enter a proper color")
    elif choice2 == "swim":
        print("Oops,You died because there are crocodiles in the river,You died, Game over.")
    else:
        print("You didn't enter a proper option")

elif choice1 == "right":
    print("Oops,You chose the wrong path,The monster ate you, You died, Game over.")
else:
    print("You didn't enter the options properly")