"""A slightly more complex form of battleship"""

__author__ = "730576169"

# Creating Boxes
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Setting variables
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
row_inbound: bool = True
column_inbound: bool = True

# picking a row by asking for an input and running a while loop if their guess is higher or than than the grid size
while row_inbound:
    row_choice: str = input("Guess a row: ")
    row_number: int = int(row_choice)
    if row_number < 1:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    elif row_number > grid_size:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    else:
        row_inbound = False

# picking column by asking for an input and running a while loop if their guess is higher or than than the grid size
while column_inbound:
    column_choice: str = input("Guess a column: ")
    column_number: int = int(column_choice)
    if column_number < 1:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    elif column_number > grid_size:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    else:
        column_inbound = False

# Checking if both guesses are and setting box for creating grid visual, also checks if one of the guesses is correct to provide a hint.
if row_number == secret_row and column_number == secret_column:
    result: str = ("Hit!")
    box: str = RED_BOX
elif row_number == secret_row and column_number != secret_column:
    result: str = ("Close! Correct row, wrong column.")
    box: str = WHITE_BOX
elif row_number != secret_row and column_number == secret_column:
    result: str = ("Close! Correct column, wrong row.")
    box: str = WHITE_BOX
else:
    result: str = ("Miss!")
    box: str = WHITE_BOX


row_count: int = 1 
while row_count <= grid_size:
    # creating a storage str
    row_str: str = str()
    column_count = 1
    # If this is the row they guessed it goes further on, else it just creates a string of blue boxes equal to the grid size
    if row_count == row_number:
        #runs a while loop for each column checking if it is the one they guessed. If it is they add the box color depending of if it was right or wrong, otherwise it adds a blue box
        while column_count <= grid_size:
            if column_count == column_number:
                row_str += str(box)
            else:
                row_str += str(BLUE_BOX)
            column_count += 1
    else: 
         while column_count <= grid_size:
             row_str += str(BLUE_BOX)
             column_count += 1
    # Prints the row output and adds 1 to start the while loop again until it does repeats equal to the number of rows
    print(row_str)
    row_count += 1
# prints whether they hit or miss or correctly geussed only one of numbers
print(result)
