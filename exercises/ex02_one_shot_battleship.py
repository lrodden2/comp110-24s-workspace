"""A slightly more complex form of battleship."""

__author__ = "730576169"

# Creating Boxes
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Setting variables. Size, row and column are adjustable and inbounds are set true to start a later while loop
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
row_inbound: bool = True
column_inbound: bool = True

# picking a row by asking for an input and running a while loop to ask them again if their guess is too high or low, if in range it sets inbound to false to end the loop
while row_inbound:
    row_choice: str = input("Guess a row: ")
    row_number: int = int(row_choice)
    if row_number < 1:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    elif row_number > grid_size:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    else:
        row_inbound = False

# Picking a column by asking for an input and running a while loop to ask them again if their guess is too high or low, if in range it sets inbound to false to end the loop
while column_inbound:
    column_choice: str = input("Guess a column: ")
    column_number: int = int(column_choice)
    if column_number < 1:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    elif column_number > grid_size:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    else:
        column_inbound = False

# Starting a row count and running a while loop until it equals grid size so it creates the proper number of rows for the grid
row_count: int = 1 
while row_count <= grid_size:
    # Creating a storage str to concatenate to later and column count to run a while loop for each box that needs to be added to the row
    row_str: str = str()
    column_count = 1
    # If this is the row they guessed it goes further on, else it just creates a string of blue boxes equal to the grid size
    if row_count == row_number:
        # Runs a while loop for each column checking if it is the one they guessed. If it is they add the box color depending of if it was right or wrong, otherwise it adds a blue box
        while column_count <= grid_size:
            if column_count == column_number:
                if column_number == secret_column and row_number == secret_row:
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
    
# Checking if both guesses are and correct to print hit, then checks if one of the guesses is correct to provide a hint, else it is a miss
if row_number == secret_row and column_number == secret_column:
    print("Hit!")
elif row_number == secret_row and column_number != secret_column:
    print("Close! Correct row, wrong column.")
elif row_number != secret_row and column_number == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")