#Tic tac toe 4*4 grid
grid=["-","-","-","-",
       "-","-","-","-",
      "-", "-", "-", "-",
      "-", "-", "-", "-"]

#current winner
winner = None

# whether the game is still going on
if_game_in_progess= True

# who is playing
present_player = "X"



def play_the_game():

    # Displays the game grid
    display_grid()

    # Loop continues until the game stops
    while if_game_in_progess:

        turn(present_player)

        check_if_game_over()

        turnover_player()

    # Since the game is over, printing the result
    if winner == "X" or winner == "O":
        print(winner + " won.")
        print("Yay! Congratulations")
    elif winner == "None":
        print("It's a Tie.")

def display_grid():
    # Displays the game grid
    print("\n")
    print(grid[0] + " | " + grid[1] + " | " + grid[2] + " | " + grid[3]      + "        0 |1 |2 |3 ")
    print(grid[4] + " | " + grid[5] + " | " + grid[6] + " | " + grid[7]      + "        4 |5 |6 |7 ")
    print(grid[8] + " | " + grid[9] + " | " + grid[10] + " | " + grid[11]    + "        8 |9 |10|11")
    print(grid[12] + " | " + grid[13] + " | "  + grid[14] + " | " + grid[15] + "        12|13|14|15")
    print("\n")
    print("\n")

def turn(player):
    # Get position from player
    print(player + "'s turn")
    position=input("Enter a position from 0-15: ")

    # to make sure it's a valid input
    valid = False
    while not valid:
        while position not in ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]:
            position= input("Enter a position from 0-15: ")

        position = int(position)
        # To make sure the spot is available in the grid
        if grid[position] =="-":
            valid = True
        else:
            return

    # Placing "X" or "O" in the grid
    grid[position] = player

    display_grid()


def turnover_player():
    # turnover the player from X to O, or O to X
    global present_player
    # if the player is X, makes it O
    if present_player == "X":
        present_player = "O"
    # if the player is O, makes it X
    elif present_player == "O":
        present_player = "X"


# Checking if the game is over
def check_if_game_over():
    checking_winner()
    checking_tie()

def checking_winner():

    global winner
    # Checking if there is a winner in rows, in columns, in diagonals.
    row_winner = checking_rows()

    column_winner = checking_columns()

    diagonal_winner = checking_diagonals()
    if row_winner:
        winner= row_winner

    elif column_winner:
        winner= column_winner

    elif diagonal_winner:
        winner= diagonal_winner

    else:
        winner = None

def checking_columns():
    global if_game_in_progress
    #checking if any of the columns have same elements.
    column1= grid[0] == grid[4] == grid[8] == grid[12] != "-"
    column2= grid[1] == grid[5] == grid[9] == grid[13] != "-"
    column3= grid[2] == grid[6] == grid[10] == grid[14] != "-"
    column4= grid[3] == grid[7] == grid[11] == grid[15] != "-"

    if column1 or column2 or column3 or  column4:
        if_game_in_progress = False
    if column1:
        return grid[0]
    elif column2:
        return grid[1]
    elif column3:
        return grid[2]
    elif column4:
        return grid[3]
    else:
        return None
def checking_rows():
    global if_game_in_progress
    # checking if any of the rows have same elements.
    row1= grid[0] == grid[1] == grid[2] == grid[3] != "-"
    row2= grid[4] == grid[5] == grid[6] == grid[7] != "-"
    row3= grid[8] == grid[9] == grid[10] == grid[11] != "-"
    row4= grid[12] == grid[13] == grid[14] == grid[15] != "-"

    if row1 or row2 or row3 or row4:
        if_game_in_progress = False
    if row1:
        return grid[0]
    elif row2:
        return grid[4]
    elif row3:
        return grid[8]
    elif row4:
        return grid[12]
    else:
        return None
def checking_diagonals():
    global if_game_in_progress
    # checking if any of the diagonals have same elements.
    diagonal1= grid[0] == grid[5] == grid[10] == grid[15] != "-"
    diagonal2= grid[3] == grid[6] == grid[9] == grid[12] != "-"


    if diagonal1 or diagonal2:
        if_game_in_progress = False
    if diagonal1:
        return grid[0]
    elif diagonal2:
        return grid[3]
    else:
        return None

# Checking if it's  a tie
def checking_tie():
    global if_game_in_progress
    if "-" not in grid:
        if_game_in_progress = False
        return True
    else:
        return False

play_the_game()



