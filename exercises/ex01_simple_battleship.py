"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730576169"


BLUE_BOX: str = "\U0001F7E6" 
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


p1_choice: str = input("Pick a secret boat location between 1 and 4: ")
p1_number: int = int(p1_choice)
if p1_number < 1:
    print(" Error!" + p1_choice + " too low!")
    exit()
if p1_number > 4:
    print(" Error!" + p1_choice + " too high!") 
    exit()


p2_choice: str = input("Guess a number between 1 and 4: ")
p2_number: int = int(p2_choice)
if p2_number < 1:
    print(" Error!" + p2_choice + " too low!") 
    exit()
if p2_number > 4:
    print(" Error!" + p2_choice + " too high!")
    exit()

if p1_number == p2_number:
    print("Correct! You hit the ship.")
    correct_result: str = RED_BOX 
    if p2_number == 1:
        print(correct_result + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if p2_number == 2:
        print(BLUE_BOX + correct_result + BLUE_BOX + BLUE_BOX)
    if p2_number == 3:
        print(BLUE_BOX + BLUE_BOX + correct_result + BLUE_BOX)
    if p2_number == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + correct_result)
    
else: 
    print("Incorrect! You missed the ship.")
    incorrect_result: str = WHITE_BOX 
    if p2_number == 1:
        print(incorrect_result + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if p2_number == 2:
        print(BLUE_BOX + incorrect_result + BLUE_BOX + BLUE_BOX)
    if p2_number == 3:
        print(BLUE_BOX + BLUE_BOX + incorrect_result + BLUE_BOX)
    if p2_number == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + incorrect_result)