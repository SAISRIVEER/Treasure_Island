print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("Your are at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if direction == 'left':
    decision = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat  or 'swim' to swim across.\n")
    if decision == 'wait':
        door_colour = input("You arrived to the island unharmed. There is a house with three doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if door_colour == 'red':
            print("Burned by fire.\nGame Over!")
        elif door_colour == 'blue':
            print("Eaten by beasts.\nGame Over!")
        elif door_colour == 'yellow':
            print("You Win!")
        else:
            print('Game Over!')
    else:
        print("Attacked by trout.\nGame Over!")

else:
    print("Fallen into a hole.\nGame Over!")

