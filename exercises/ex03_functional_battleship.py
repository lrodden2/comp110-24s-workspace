"""Functional Battleship with Functions."""

__author__ = "730576169"

# Imports random for later use of randint
import random

# Imports box for printing the grid
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_size: int, side_choice: str) -> int:
    """Asks for input from the user.."""
    assert side_choice == "row" or side_choice == "column"
    inbound: bool = True
    # While statement that prompts for input and reasks if it is out of the range, and pairs that with either a row or column
    while inbound:
        side_guess: str = input(f"Guess a {side_choice}: ")
        side_number: int = int(side_guess)
        if side_number < 1:
            print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
        elif side_number > grid_size:
            print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
        else:
            inbound = False
    return side_number


def print_grid(grid_size: int, row_guess: int, column_guess: int, user_correct: bool) -> None:
    """Function that prints the result."""
    # Starting a row count and running a while loop until it equals grid size so it creates the proper number of rows for the grid
    row_count: int = 1 
    while row_count <= grid_size:
        # Creating a storage str to concatenate to later and column count to run a while loop for each box that needs to be added to the row
        row_str: str = str()
        column_count = 1
    # If this is the row they guessed it goes further on, else it just creates a string of blue boxes equal to the grid size
        if row_count == row_guess:
            # Runs a while loop for each column checking if it is the one they guessed. If it is they add the box color depending of if it was right or wrong, otherwise it adds a blue box
            while column_count <= grid_size:
                if column_count == column_guess:
                    if user_correct is True:
                        row_str += str(RED_BOX)
                    else:
                        row_str += str(WHITE_BOX) 
                else:
                    row_str += str(BLUE_BOX)
                column_count += 1
        else: 
            while column_count <= grid_size:
                row_str += str(BLUE_BOX)
                column_count += 1
    # Prints the row output and adds 1 to start the while loop again until it does repeats equal to the number of rows and matches the grid size
        print(row_str)
        row_count += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Checks if the guess is correct."""
    # Just checks if both guesses are accurate to be true
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Main program for Battleship."""
    # Creates a variable for the number of turns. Also starts a turn counter of 1 and creates a positive bool either of which can exit the while loop
    turn_number: int = 5
    turn_count: int = 1
    hit_correct: bool = True
    while turn_count <= turn_number and hit_correct:
        # Prints the current turn out of the total turn numbers
        print(f"=== Turn {turn_count}/{turn_number} ===")
        # Asks for input with the input_guess function, with the designation set to row that to be row_guess
        row_guess: int = input_guess(grid_size, "row")
        # Asks for input with the input_guess function, with the designation set to column and sets that to be column_guess
        column_guess: int = input_guess(grid_size, "column")
        # Checks if the input is accurate or not with correct_guess function
        result: bool = correct_guess(secret_row, secret_column, row_guess, column_guess)
        # If they are correct, it uses print_grid based on the grid size and both guesses with the bool set to True as they were correct and prints that they won, hit_correct is then set to false to end the loop
        if result is True:
            print_grid(grid_size, row_guess, column_guess, True)
            print(f"You won in {turn_count}/{turn_number} turns!")
            hit_correct = False
        # If incorrect it uses print_grid based on the grid size and both guesses with the bool set to False, it then prints miss and adds to the turn count. If the turn count is met then if prints an extra message before the program ends
        else:
            print_grid(grid_size, row_guess, column_guess, False)
            print("Miss!")
            turn_count += 1
            if turn_count > turn_number:
                print("X/5 - Better luck next time!")

    
# Sets the grid size, secret row, and secret column to be a random number to create a game you can play
if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))