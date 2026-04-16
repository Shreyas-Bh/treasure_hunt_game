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
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
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
print("You are at a cross road. Where do you want to go?")

turn = input("Type \"left\" or \"right\".\n")
if turn == "left":
    print("You have reached the shore. Do you want to wait for a boat or swim?")
    wait = input("Type \"wait\" to wait for the boat. Type \"swim\" to swim across.\n")
    if wait == "wait":
        print("You have crossed the shore easily, but there are 3 doors to exit, which one would you pick?")
        exit = input("Pick one door to exit, \"red\", \"blue\", \"yellow\".\n")
        if exit == "red":
            print("Game over. You entered the devils house")
        elif exit == "blue":
            print("Game Over. You drowned into the ocean")
        elif exit == "yellow":
            print("Congratulation! You can take home the treasure.")
        else:
            print("Please check the selection you have made.")
    else:
        print("Game Over")
elif turn == "right":
    print("Game Over")
else:
    print("Please check the selection you have made & retry. ")
