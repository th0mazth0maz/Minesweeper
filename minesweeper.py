import random,sys,time
#Function for planting bombs on the board.
def plant_bombs(board):
    count = 0
    global bombLocation
    bombLocation = []
    #Conditional while loop that will repeat until number of bombs specified by difficulty is planted on the board.
    while count < bombCount:
        #Generates random values between 0 and the max row value or max column value on the board.
        row = random.randint(0, maxRow - 1)
        col = random.randint(0, maxCol - 1)
        #Centre is equal to bomb location and is used as a central position point while incrementing clue locations around the bomb on the board. 
        centre = board[row][col]
        #if statement will ensure multiple bombs are not placed on a single position. 
        if (centre != "*"):
            board[row][col] = "*"
            #If a clue or empty cell is present centre right from the bomb it will be incremented.
            if (col >= 0 and col <= maxCol - 2) and (row >= 0 and row <= maxRow - 1):
                if (board[row][col + 1] == ' '):
                    board[row][col + 1] = 1
                elif (board[row][col + 1] != '*' and board[row][col + 1] != ' '):
                    board[row][col + 1] += 1
            #If a clue or empty cell is present centre left from the bomb it will be incremented. 
            if (col >= 1 and col <= maxCol - 1) and (row >= 0 and row <= maxRow - 1):
                if (board[row][col - 1] == ' '):
                    board[row][col - 1] = 1
                elif (board[row][col - 1] != '*' and board[row][col - 1] != ' '):
                    board[row][col - 1] += 1
            #If a clue or empty cell is present top left from the bomb it will be incremented. 
            if (col >= 1 and col <= maxCol - 1) and (row >= 1 and row <= maxRow - 1):
                if (board[row - 1][col - 1] == ' '):
                    board[row - 1][col - 1] = 1
                elif (board[row - 1][col - 1] != '*' and board[row - 1][col - 1] != ' '):
                    board[row - 1][col - 1] += 1
            #If a clue or empty cell is present top right from the bomb it will be incremented.
            if (col >= 0 and col <= maxCol - 2) and (row >= 1 and row <= maxRow - 1):
                if (board[row - 1][col + 1] == ' '):
                    board[row - 1][col + 1] = 1
                elif (board[row - 1][col + 1] != '*' and board[row - 1][col + 1] != ' '):
                    board[row - 1][col + 1] += 1
            #If a clue or empty cell is present top centre from the bomb it will be incremented. 
            if (col >= 0 and col <= maxCol - 1) and (row >= 1 and row <= maxRow - 1):
                if (board[row - 1][col] == ' '):
                    board[row - 1][col] = 1
                elif (board[row - 1][col] != '*' and board[row - 1][col] != ' '):
                    board[row - 1][col] += 1
            #If a clue or empty cell is present bottom right from the bomb it will be incremented. 
            if (col >= 0 and col <= maxCol - 2) and (row >= 0 and row <= maxRow - 2):
                if (board[row + 1][col + 1] == ' '):
                    board[row + 1][col + 1] = 1
                elif (board[row + 1][col + 1] != '*' and board[row + 1][col + 1] != ' '):
                    board[row + 1][col + 1] += 1 
            #If a clue or empty cell is present bottom left from the bomb it will be incremented.
            if (col >= 1 and col <= maxCol - 1) and (row >= 0 and row <= maxRow - 2):
                if (board[row + 1][col - 1] == ' '):
                    board[row + 1][col - 1] = 1
                elif (board[row + 1][col - 1] != '*' and board[row + 1][col - 1] != ' '):
                    board[row + 1][col - 1] += 1 
            #If a clue or empty cell is present bottom centre from the bomb it will be incremented. 
            if (col >= 0 and col <= maxCol - 1) and (row >= 0 and row <= maxRow - 2):
                if (board[row + 1][col] == ' '):
                    board[row + 1][col] = 1
                elif (board[row + 1][col] != '*' and board[row + 1][col] != ' '):
                    board[row + 1][col] += 1 
            #Create array to store information about bomb location for hint
            bomb = [row,col]
            bombLocation.append(bomb)
            #Increment to show successful bomb plant *boom*
            count = count + 1
    #Returns the board back to 'create_game_board' function.       
    return board

#Function to return a completed game board back to the main game. 
def create_game_board(maxRow, maxCol):
    #This line creates 2D array board with empty strings spaces in each list item. Size depends on 'maxCol' and 'maxRow' which depends on game difficulty.
    board = [[' ' for col in range(maxCol)] for row in range(maxRow)]
    #Calls 'plant_bombs' function to plant bombs on the board, and create clue positions. 
    board = plant_bombs(board)
    #Returns completed board back to the main game. 
    return board

#Function to return a completed true/false board, similar in size to game board, to show whether position has been opened. 
def create_opened_cells_board(maxRow, maxCol):
    #This line creates 2D array board with False boolean statement in it. Size depends on 'maxCol' and 'maxRow' which depends on game difficulty. 
    openedCells = [[False for col in range(maxCol)] for row in range(maxRow)]
    #Returns completed true/false board to show open positions. 
    return openedCells

#Procedure used to print the game board during game play. 
def print_board(board,is_cell_open,flagged_cells):
    num_of_rows = len(board)
    num_of_columns = len(board[0])
    columns_id  = range(0,num_of_columns)
    print('\t', end='') # Required for proper visualization of the columns' id numbers
    for id in columns_id: # Print the id numbers of columns
        print(id,'\t',end='')  # the end='' prevents print to change line
    print('\n')
    print('\t', end='')
    for id in columns_id:
        print('_', '\t', end='')
    print('\n')
    for board_row in range(num_of_rows):
        print(board_row,'| ','\t',end='') # Print the id numbers of rows
        for board_column in range (num_of_columns):
            if is_cell_open[board_row][board_column]:# For each cell in the board, check if it is opened by the player
                print(board[board_row][board_column],'\t',end='')
            elif [board_row,board_column] in flagged_cells: # if the cell is flagged as mine by the player print F
                print('F', '\t', end='')
            else: # Print X if the cell is not open
                print('X''\t',end='')
        print('\n')

#Procedure to give hint to the player.
def give_hint():
    #Declare global variable from 'plant_bombs' function.
    global bombLocation
    #Select random number, and then use that to choose which hint to give, this is printed to the terminal.
    selection = random.randint(0, bombCount - 1)
    print("Location of a bomb on the map: ", bombLocation[selection])

#Procedure to check whether a flag has been placed on open positions, used in the 'open_empty' function and in the main game play.
def flag_check(row, col):
    #Sets 'length' value to the number of items in the 'flaggedCells' array.
    length = len(flaggedCells)
    #'row' and 'col' values are put into a similar format in the 'currentPosition' as the 'flaggedCells' formart so they can be compared. 
    currentPosition = "[{}][{}]".format(row, col)
    i = 0
    #for loop lets us search through 'flaggedCells' array.
    for i in range(length):
        #If there is a match between 'flaggedCells' and 'currentPosition' and the 'currentPosition' is opened, then that flag position is removed from 'flaggedCells'
        if (flaggedCells[i] == currentPosition):
            if (openedCells[row][col] == True):
                flaggedCells.pop(i)

#Function used to open multiple empty positions on the game board, this is done using recursion to keep checking unchecked positions until all are found and opened. 
def open_empty (board, openedCells, row, col):
    #Code to check centre left position from the centre.
    if (col >= 1 and col <= maxCol - 1) and (row >= 0 and row <= maxRow - 1):
        #if statement to check the centre left position is empty and unopened, and then open the cell and call 'flag_check' procedure to remove any flags. 
        if ((board[row][col - 1] == " ") and (openedCells[row][col - 1] != True)):
            openedCells[row][col - 1] = True
            flag_check(row, col - 1)
            #Code calls the 'open_empty' function within the function to keep searching the board further, it is recursive. Centre left becomes centre.
            openedCells = open_empty(board, openedCells, row, col - 1)
        #elif statement to check the centre left position is not empty, and then cell is opened 'flag_checked' is called, but no 'open_empty' function is called and recursion stops.
        elif (board[row][col - 1] != " "):
            openedCells[row][col - 1] = True
            flag_check(row, col - 1)
    #Code to check top left position from the centre.
    if (col >= 1 and col <= maxCol - 1) and (row >= 1 and row <= maxRow - 1):
        #if statement to check the top left position is empty and unopened, and then open the cell and call 'flag_check' procedure to remove any flags. 
        if ((board[row - 1][col - 1] == " ") and (openedCells[row - 1][col - 1] != True)):
            openedCells[row - 1][col - 1] = True
            flag_check(row - 1, col - 1)
            #Code calls the 'open_empty' function within the function to keep searching the board further, it is recursive. Top left becomes centre.
            openedCells = open_empty(board, openedCells, row - 1, col - 1)
        #elif statement to check the top left position is not empty, and then cell is opened and 'flag_check' is called, but no 'open_empty' function is called and recursion stops. 
        elif (board[row - 1][col - 1] != " "):
            openedCells[row - 1][col - 1] = True
            flag_check(row - 1, col - 1)
    #Code to check top centre position from the centre.
    if (col >= 0 and col <= maxCol-1) and (row >= 1 and row <= maxRow - 1):
        #if statement to check the top centre position is empty and unopened, and then open the cell and call 'flag_check' procedure to remove any flags. 
        if ((board[row - 1][col] == " ") and (openedCells[row - 1][col] != True)):
            openedCells[row - 1][col] = True
            flag_check(row - 1, col)
            #Code calls the 'open_empty' function within the function to keep searching the board further, it is recursive. Top centre becomes centre.
            openedCells = open_empty(board, openedCells, row - 1, col)
        #elif statement to check the top centre position is not empty, and then cell is opened and 'flag_check' is called, but no 'open_empty' function is called and recursion stops.
        elif (board[row - 1][col] != " "):
            openedCells[row - 1][col] = True
            flag_check(row - 1, col)
    #Code to check top right position from the centre. 
    if (col >= 0 and col <= maxCol - 2) and (row >= 1 and row <= maxRow - 1):
        #if statement to check the top right position is empty and unopened, and then open the cell and call 'flag_check' procedure to remove any flags. 
        if ((board[row - 1][col + 1] == " ") and (openedCells[row - 1][col + 1] != True)):
            openedCells[row - 1][col + 1] = True
            flag_check(row - 1, col + 1)
            #Code calls the 'open_empty' function within the function to keep searching the board further, it is recursive. Top right becomes centre. 
            openedCells = open_empty(board, openedCells, row - 1, col + 1)
        #elif statement to check the top right position is not empty, and then cell is opened and 'flag_check' is called, but no 'open_empty' function is called and recursion stops. 
        elif (board[row - 1][col + 1] != " "):
            openedCells[row - 1][col + 1] = True
            flag_check(row - 1, col + 1)
    #Code to check centre right position from the centre.
    if (col >= 0 and col <= maxCol - 2) and (row >= 0 and row <= maxRow - 1):
        #if statement to check the centre right position is empty and unopened, and then open the cell and call 'flag_check' procedure to remove any flags. 
        if ((board[row][col + 1] == " ") and (openedCells[row][col + 1] != True)):
            openedCells[row][col + 1] = True
            flag_check(row, col + 1)
            #Code calls the 'open_empty' function within the function to keep searching the board further, it is recursive. Centre right becomes centre.
            openedCells = open_empty(board, openedCells, row, col + 1)
        #elif statement to check the centre right position is not empty, and then cell is opened and 'flag_check' is called, but no 'open_empty' function is called and recursion stops. 
        elif (board[row][col + 1] != " "):
            openedCells[row][col + 1] = True
            flag_check(row, col + 1)
    #Code to check bottom right position from the centre. 
    if (col >= 0 and col <= maxCol -2) and (row >= 0 and row <= maxRow - 2):
        #if statement to check the bottom right position is empty and unopened, and then open the cell and call 'flag_check' procedure to remove any flags. 
        if ((board[row + 1][col + 1] == " ") and (openedCells[row + 1][col + 1] != True)):
            openedCells[row + 1][col + 1] = True
            flag_check(row + 1, col + 1)
            #Code calls the 'open_empty' function within the function to keep searching the board further, it is recursive. Bottom right becomes centre. 
            openedCells = open_empty(board, openedCells, row + 1, col + 1)
        #elif statement to check the bottom right position is not empty, and then cell is opened and 'flag_check' is called, but no 'open_empty' function is called and recursion stops.
        elif (board[row + 1][col + 1] != " "):
            openedCells[row + 1][col + 1] = True
            flag_check(row + 1, col + 1)
    #Code to check bottom centre position from the centre. 
    if (col >= 0 and col <= maxCol - 1) and (row >= 0 and row <= maxRow - 2):
        #if statement to check the bottom centre position is empty and unopened, and then open the cell and call 'flag_check' procedure to remove any flags. 
        if ((board[row + 1][col] == " ") and (openedCells[row + 1][col] != True)):
            openedCells[row + 1][col] = True
            flag_check(row + 1, col)
            #Code calls the 'open_empty' function within the function to keep searching the board further, it is recursive. Bottom centre becomes centre.
            openedCells = open_empty(board, openedCells, row + 1, col)
        #elif statement to check the bottom centre position is not empty, and then cell is opened and 'flag_check' is called, but no 'open_empty' function is called and recursion stops.
        elif (board[row + 1][col] != " "):
            openedCells[row + 1][col] = True
            flag_check(row + 1, col)
    #Code to check bottom left position from the centre.
    if (col >= 1 and col <= maxCol - 1) and (row >= 0 and row <= maxRow - 2):
        #if statement to check the bottom left position is empty and unopened, and then open the cell and call 'flag_check' procedure to remove any flags.
        if ((board[row + 1][col - 1] == " ") and (openedCells[row + 1][col - 1] != True)):
            openedCells[row + 1][col - 1] = True
            flag_check(row + 1, col - 1)
            #Code calls the 'open_empty' function within the function to keep searching the board further, it is recursive. Bottom left becomes centre. 
            openedCells = open_empty(board, openedCells, row + 1, col + 1)
        #elif statement to check the bottom left position is not empty, and then cell is opened and 'flag_check' is called, but no 'open_empty' function is called and recursion stops.
        elif (board[row + 1][col - 1] != " "):
            openedCells[row + 1][col - 1] = True
            flag_check(row + 1, col - 1)
    return openedCells

def get_leaderboard():
    #if statement in case the outcome of the game is a win.
    if (win == True):
        #Will open the 'leaderboard.txt' file to append it.
        with open('leaderboard.txt', 'a') as leaderboardFile:
            #These if/else statements decide what is written to the 'leaderboard.txt' file for the game difficulty.
            if (difficulty == "e"):
                leaderboardDifficulty = "Easy"
            elif (difficulty == "m"):
                leaderboardDifficulty = "Medium"
            elif (difficulty == "h"):
                leaderboardDifficulty = "Hard"
            #Will write to the 'leaderboard.txt' file in the format: Time: 00:05:12 | Name: Tom | Difficulty: Easy
            leaderboardFile.write("Time: {} | Name: {} | Difficulty: {} \n".format(finishTime, username, leaderboardDifficulty))
            #Close the 'leaderboard.txt' file.
            leaderboardFile.close
        #Will open the 'leaderboard.txt' file to read it. 
        with open('leaderboard.txt', 'r') as leaderboardFile:
            #Take each line and put it into 'leaderboard' array.
            leaderboard = leaderboardFile.readlines()
            #Will sort the items of the 'leaderboard' array into ascending value.
            leaderboard.sort()
            leaderboardLength = len(leaderboard)
            print("")
            print("-- Leaderboard --")
            print("")
            i = 0
            #for loop will loop through each item of the 'leaderboard' array, printing it and creating the leaderboard. 
            for i in range(leaderboardLength):
                print(leaderboard[i], end='')
                print("\n")
    #elif statement in case the outcome of the game is a loss.
    elif (win == False):
        #Will open the 'leaderboard.txt' file to read it.
        with open('leaderboard.txt', 'r') as leaderboardFile:
            #Take each line and put it into 'leaderboard' array.
            leaderboard = leaderboardFile.readlines()
            #Will sort the items of the 'leaderboard' array into ascending value.
            leaderboard.sort()
            leaderboardLength = len(leaderboard)
            print("")
            print("-- Leaderboard --")
            print("")
            i = 0
            #for loop will loop through each item of the 'leaderboard' array, printing it and creating the leaderboard.
            for i in range(leaderboardLength):
                print(leaderboard[i], end='')
                print("\n")

#Function to format time value from 'endTime' and 'startTime'.
def time_format():
    #To find the difference.
    timeLapsed = endTime - startTime
    #Format the difference value into time, giving hours, minutes and seconds. 
    sec = timeLapsed
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    finishTime = ("{:0>2,}:{:0>2,}:{:0>2,}".format(int(hours), int(mins), int(sec)))
    #Formatted time returned to the main module. 
    return finishTime

#Beginning of game play!
print("Minesweeper Game!")
print("")
#Input username, used later for the leaderboard.
username = input("What is your name? ")
print("")
#'validInput' and while loop are used to validate the input of user, ensuring that the program won't fail later on.
validInput = False
while (validInput == False):
    #'mode' is the difficulty setting for the game, these will alter the game board size and the number of bombs on the board.
    difficulty = (input("What game difficulty would you like to play? \n'h' - hard, 'm' - medium, 'e' - easy: "))
    print("")
    if (difficulty == "h") or (difficulty == "m") or (difficulty == "e"):
        validInput = True
    else:
        print("Invalid input, please try again.")
#'flaggedCells' will store the placed flag positioned, needed for the 'print_board' procedure.
flaggedCells = []
#if statements that assign the maximum row and maximum column parameters and the bomb count based on the game difficulty.
if (difficulty == 'e'):
    maxRow = 9
    maxCol = 9
    bombCount = 10
elif (difficulty == 'm'):
    maxRow = 16
    maxCol = 16
    bombCount = 40
elif (difficulty == 'h'):
    maxRow = 30
    maxCol = 16
    bombCount = 99
#Calls the 'create_game_board' function to create the game board.
board = create_game_board(maxRow, maxCol)
print (board)
#Calls the 'create_opened_cells_board' function to create the board which determines which cells have been opened.
openedCells = create_opened_cells_board(maxRow, maxCol)
#'print_board' procedure will print the game board to the terminal.
print_board(board, openedCells, flaggedCells)
#Sets number of unflagged bombs to equal number initally planted on the board.
unflaggedBombs = bombCount
#Number of unflagged bombs shown to user.
print("Remaining unflagged mines:", unflaggedBombs, "\n", end="")
print("")
endGame = False
win = False
flaggedBombs = 0
#Starts the timer by getting the initial time value.
startTime = time.time()
#while loop allows the player to carry out multiple actions on the board and select multiple points while the game is running.
while (endGame == False):
    #Below code will take in the row and column values and ensure they are valid based on the difficulty level and board size. 
    validInput = False
    print("What position would you like to select next?")
    row = int(input("Row: "))
    col = int(input("Column: "))
    print("")
    #Validating 'row' and 'col' value for easy difficulty.
    if (difficulty == "e"):
        if (row >= 0 and row <= 8):
            if (col >= 0 and row <= 8):
                validInput = True
    #Validating 'row' and 'col' value for medium difficulty.
    elif (difficulty == "m"):
        if (row >= 0 and row <= 15):
            if (col >= 0 and row <= 15):
                validInput = True
    #Validating 'row' and 'col' value for hard difficulty.
    elif (difficulty == "h"):
        if (row >= 0 and row <= 29):
            if (col >= 0 and col <= 15):
                validInput = True
    #If 'row' or 'col' values invalid then output given to user, and the section of code will loop to let user reenter values. 
    if (validInput == False):
        print("Invalid input, please try again")
    #If 'row' or 'col' values valid then the code will let the user continue onto perform an action. 
    if (validInput == True):
        #Code below will ensure that a valid input is given for 'action' value, avoids any errors occuring. 
        validInput = False
        while (validInput == False):
            action = (input("Choose the action that will be taken on this position... \n'f' - flag, 'r' - remove flag, 'd' - dig up: "))
            print("")
            if (action == "f") or (action == "r") or (action == "d"):
                validInput = True
            else: 
                print("Input invalid, please try again.")
        #if statement will branch to execute code to flag a position on the board. 
        if (action == 'f'):
            count = 0
            duplicate = False
            #Create the 'flag' variable to be inserted into the 'flaggedCells' array later. 
            flag = [row,col]
            #for loop is used to search for the 'flag' value in the 'flaggedCells' array to ensure the position has not already been flagged. 
            for count in range(0, len(flaggedCells)):
                if (flaggedCells[count] == flag):
                    duplicate = True
            #if statement branches to place the flag if the position does not already have a flag and has not already been dug. 
            if (duplicate == False and openedCells[row][col] == False):
                #Appends 'flaggedCells' array to add the 'flag' value.
                flaggedCells.append(flag)
                #if statement to branch if a bomb is located under the flag, and increments the 'flaggedBombs' value. 
                if (board[row][col] == "*"):
                    flaggedBombs += 1
                    #if statement to branch if all the bombs on the board are flagged, this then goes to tell the user they have won the game. 
                    if (flaggedBombs == bombCount):
                        endGame = True
                        win = True
                        #for loops will set all positions on the 'openedCells' board to True, so that they fully opened board can be shown to the user. 
                        for row in range (0, maxRow):
                            for col in range (0, maxCol):
                                if (board[row][col] != "*"):
                                    openedCells[row][col] = True
                        print_board(board, openedCells, flaggedCells)
                        print("\nThe game has ended. You've won.\n", end="")
                        #break used to skip the hint section of code. 
                        break
                    #else statement to branch if any flags have not been found yet, this will 'print_board' and then calculate and display remaining unflagged bombs. 
                    else:
                        print_board(board, openedCells, flaggedCells)
                        unflaggedBombs = bombCount - flaggedBombs
                        print("Remaining unflagged mines:", unflaggedBombs, "\n", end="")
                else:
                    print_board(board, openedCells, flaggedCells)
                    unflaggedBombs = bombCount - flaggedBombs
                    print("Remaining unflagged mines:", unflaggedBombs, "\n", end="")
            #elif statement incase there is already a flag in the position, while loop will take them back to section to input a different position.
            elif (duplicate == True):
                print ("Flag has already been placed here")
            #elif statement incase the position has already been opened, while loop take them back to section to input a different position. 
            elif (openedCells[row][col] == True):
                print ("Flag cannot be placed on open cell")
        #if statement will branch to execute code to remove a flag from a position on the board.
        elif (action == 'r'):
            count = 0
            unflagged = False
            #Create the 'flag' variable so it can be searched for and removed from the 'flaggedCells' array later.
            flag = [row, col]
            #for loop to go through each item in the array.
            for count in range (0, len(flaggedCells)):
                #if statement to branch if 'flag' value matches an item in the 'flaggedCells' array, that item is then removed from the array.
                if (flaggedCells[count] == flag):
                    flaggedCells.pop(count)
                    #if statement to decide whether a bomb was present under the unflagged position, if so it will update the 'flaggedBombs' value.
                    if (board[row][col] == "*"):
                        flaggedBombs = flaggedBombs - 1
                    #'print_board' and then calculate and display remaining unflagged bombs. 
                    print_board(board, openedCells, flaggedCells)
                    unflaggedBombs = bombCount - flaggedBombs
                    print("Remaining unflagged mines:", unflaggedBombs, "\n", end="")
                    unflagged = True
            #if statement in case no flag was found on the position.
            if (unflagged == False):
                print("No flag has been placed here")
        #if statement will branch to execute code to dig a section of the board.
        elif (action == 'd'):
            #if statement to check that the position is unopened.
            if (openedCells[row][col] == False):
                #Position is them opened on the 'openedCells' board.
                openedCells[row][col] = True
                #Flag check ensure that a flag is removed after being opened.
                flag_check(row, col)
                #if statement in case a position is being opened with a bomb in that position. 
                if (board[row][col] == '*'):
                    endGame = True
                    win = False
                    for row in range (0, maxRow):
                        for col in range (0, maxCol):
                            openedCells[row][col] = True
                    print_board(board, openedCells, flaggedCells)
                    print("\nThe game has ended. You've lost.\n", end="")
                    #break used to skip the hint section of code. 
                    break
                #elif statement in case an empty position is being opened, will then call a recursive function to open surrounding cells.
                elif (board[row][col] == ' '):
                    #Calls recursive function that will check surrounding cells to see if they are empty and open them is so. 
                    openedCells = open_empty(board, openedCells, row, col)
                    #'print_board' and then calculate and display remaining unflagged bombs. 
                    print_board(board, openedCells, flaggedCells)
                    unflaggedBombs = bombCount - flaggedBombs
                    print("Remaining unflagged mines:", unflaggedBombs, "\n", end="")
                #else statement will handle position that contain clues.
                else:
                    #'print_board' and then calculate and display remaining unflagged bombs. 
                    print_board(board, openedCells, flaggedCells)
                    unflaggedBombs = bombCount - flaggedBombs
                    print("Remaining unflagged mines:", unflaggedBombs, "\n", end="")
            #else statement in case the selected position has already been opened. 
            else:
                print("This position has already been dug")
        #Final section of the while loop will handle the hint function of the code. 
        validInput = False
        #Takes input for the 'hintOption' and ensures it is a valid input. 
        while (validInput == False):
            print("")
            hintOption = (input("Would you like a hint revealed? \n'h' - for hint, 'n' - for no hint: "))
            if (hintOption == "h") or (hintOption == "n"):
                validInput = True
                #if statement for if a hint has been selected, this calls function to output hint to user. 
                if (hintOption == "h"):
                    give_hint()
                    print("")
                if (hintOption == "n"):
                    print("")
            #else statement to handle invalid input.
            else:
                print("")
                print("Invalid input, please try again.")

#Ends the timer by getting the final time value.
endTime = time.time()
#Calls 'time_format()' function to retrieve the play time that has been calculated and formatted.
finishTime = time_format()
#Calls procedure that will print the leaderboard to the terminal.
get_leaderboard()