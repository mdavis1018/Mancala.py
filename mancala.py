"""
File:    mancala.py                                                               
Author:  Marcus Davis                                                                     
Date:    11/3/2023                                                                        
Section: 58-Dis(8021)                                                                     
E-mail:  marcusd2@umbc.edu                                                                
Description: creates a mancala game and allows two users to play
"""
game_over = False
BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '
top_cups = [
    ["Cup", "1", "Stones", "  4   ", "      ", "[ 6 ]"],
    ["Cup", "2", "Stones", "  4   ", "      ", "[ 6 ]"],
    ["Cup", "3", "Stones", "  4   ", "      ", "[ 6 ]"],
    ["Cup", "4", "Stones", "  4   ", "      ", "[ 6 ]"],
    ["Cup", "5", "Stones", "  4   ", "      ", "[ 6 ]"],
    ["Cup", "6", "Stones", "  4   ", "      ", "[ 6 ]"]

]
bottom_cups = [
    ["Cup", "13", "Stones", "  4   ", "      ", "[ 6 ]"],
    ["Cup", "12", "Stones", "  4   ", "      ", "[ 5 ]"],
    ["Cup", "11", "Stones", "  4   ", "      ", "[ 6 ]"],
    ["Cup", "10", "Stones", "  4   ", "      ", "[ 6 ]"],
    ["Cup", "9", "Stones", "  4   ", "      ", "[ 6 ]"],
    ["Cup", "8", "Stones", "  4   ", "      ", "[ 6 ]"]
]

mancala_a = [
    "      ",  # Row 1
    "      ",  # Row 2
    "      ",  # Row 3
    "      ",  # Row 4
    "      ",  # Row 5
    "******",  # Row 6
    "      ",  # Row 7
    "      ",  # Row 8
    "      ",  # Row 9
    "      ",  # Row 10
    "      "   # Row 11
]

mancala_b = [
    "      ",  # Row 1
    "      ",  # Row 2
    "      ",  # Row 3
    "      ",  # Row 4
    "      ",  # Row 5
    "******",  # Row 6
    "      ",  # Row 7
    "      ",  # Row 8
    "      ",  # Row 9
    "      ",  # Row 10
    "  B  "    # Row 11
]
player_1_points = 0
player_2_points = 0


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    """                                                                                                    
   draw_board is the function that you should call in order to draw the board.                            
       top_cups and bottom_cups are lists of strings.  Each string should be length BLOCK_WIDTH and each \
list should be of length BLOCK_HEIGHT.                                                                     
       mancala_a and mancala_b should be 2d lists of strings.  Each string should be BLOCK_WIDTH in lengt\
h, and each list should be 2 * BLOCK_HEIGHT + 1                                                            

   :param top_cups: This should be a list of strings that represents cups 1 to 6 (Each list should be at \
least BLOCK_HEIGHT in length, since each string in the list is a line.)                                    
   :param bottom_cups: This should be a list of strings that represents cups 8 to 13 (Each list should be\
at least BLOCK_HEIGHT in length, since each string in the list is a line.)                                
   :param mancala_a: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala\
at position 7.                                                                                            
   :param mancala_b: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala\
at position 0.                                                                                            
   """
    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)]
             for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    # draw midline
    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)
    print('\n'.join([''.join(board[i]) for i in range(len(board))]))


def draw_mancala(fore_or_aft, mancala_data, the_board):
    """                                                                                                    
       Draw_mancala is a helper function for the draw_board function.                                     
   :param fore_or_aft: front or back (0, or 1)                                                            
   :param mancala_data: a list of strings of length 2 * BLOCK_HEIGHT + 1 each string of length BLOCK_WIDT\
H                                                                                                          
   :param the_board: a 2d-list of characters which we are creating to print the board.                    
   """
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) -
                                 BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
    """Draw block is a helper function for the draw_board function.                                       
   :param the_board: the board is the 2d grid of characters we're filling in                              
   :param pos_x: which cup it is                                                                          
   :param pos_y: upper or lower                                                                           
   :param block_data: the list of strings to put into the block.                                          
   """
    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[
                j]


def get_player():
    """
    Gets the names of two players
    """

    player_1 = ""
    player_2 = ""
    for i in range(2):
        player_1 = input("Please tell me your name: ")
        player_2 = input("Please tell me your name: ")
        break
    return player_1, player_2
    pass


def run_game(game_over):
    """
    :param: takes the boolean true/false in order to run or end the game
    Master function. Runs the game by calling other functions. Sets some important variables to pass into other functions
    """
    if not game_over:  # if the game isn't over(no row is empty)
        player_1, player_2 = get_player()
        mancala_a[2] = player_1[:6].ljust(6)
        mancala_b[8] = player_2[:6].ljust(6)
        draw_board(top_cups, bottom_cups, mancala_a, mancala_b)
        player = (player_1, player_2)
        while not game_over:  # Keep the game running until it's over
            take_turn(player)
            if game_over:
                print("Game over.")
                track_points(player_1, player_2)
                break

    pass


def distribute_stones(cups, distribute_cup, num_stones):
    """
    :param cups: the combined list of top/bottom cups
    :param distribute_cup: the unedited integer the user enters to select which cup to take stones from
    :param num_stones: the number of stones inside the cup the user selected
    """
    global player_1_points
    global player_2_points
    top_cups = cups[:6]  # splicing cups into top
    bottom_cups = cups[6:12]  # splicing cups into bottom
    bottom_cups = bottom_cups[::-1]  # reversing bottom list
    cups = top_cups + bottom_cups
    current_cup = distribute_cup
    previous = ''
    while num_stones > 0:
        # if the next cup is the one after 13 loop it around to 1
        if (current_cup + 1 == 14) or (current_cup == 14):
            current_cup = 0
        # Place a stone in the current cup
        if current_cup >= 8:
            cups[current_cup - 1][3] = str(int(cups[current_cup - 1][3]) + 1)
        else:
            cups[current_cup][3] = str(int(cups[current_cup][3]) + 1)

        # if we reach the mancala on the right subtract one extra stone and add a point
        if cups[current_cup - 1][1] == '8':
            num_stones -= 1
            player_1_points += 1

        # if we reach the mancala on the left subtract one extra stone and add a point
        if ((cups[current_cup - 1][1] == '1') and (previous == '13')):
            player_2_points += 1
            num_stones -= 1
        previous = cups[current_cup - 1][1]
        current_cup += 1
        num_stones -= 1


def track_points(player_1, player_2):
    """
    :param player_1: the first player
    :param player_2: the second player
    """
    global player_1_points
    global player_2_points
    # uses the global variables to keep track of the score
    print(f"{player_1} Score: {player_1_points}, {player_2} Score: {player_2_points}")


def detect_win(cups, player_1, player_2):
    """
    :param cups: combined list of bottom and top cups
    :param player_1: first player
    :param player_2: second player
    """
    global game_over
    global player_1_points
    global player_2_points

    if all(int(cup[3]) == 0 for cup in cups[:6]):  # if the top row is empty
        game_over = True
        print("Game Over")
        if player_1_points > player_2_points:
            print(f"{player_1} WINS!!")
        elif player_2_points > player_1_points:
            print(f"{player_2} WINS!!!")

    if all(int(cup[3]) == 0 for cup in cups[6:12]):  # if the bottom row is empty
        game_over = True
        if player_1_points > player_2_points:
            print(f"{player_1} WINS!!")
        elif player_2_points > player_1_points:
            print(f"{player_2} WINS!!!")
        print("Game Over")


def take_turn(player):
    """
    param: player: combined list of both players
    """
    global top_cups
    global bottom_cups
    global game_over
    global player_1_points
    global player_2_points
    combined_cups = top_cups + bottom_cups
    print(combined_cups[8])
    player_1 = player[0]
    player_2 = player[1]
    players_turn = player_1  # used to alternate between player turns
    while True:
        if players_turn == player_1:  # player 1 turn
            selection = int(
                input(f"It is {players_turn}'s turn. Enter a cup (1-13) "))
            distribute_cup = selection
            # user must input a number within this range
            if not ((1 <= selection <= 6) or (8 <= selection <= 13)):
                print("Enter a cup number 1-13 (not 7)")
                continue
            if selection >= 7:  # changes the index of the cups array i'm calling
                if selection == 7:
                    selection = 13
                elif selection == 8:
                    selection = 12
                elif selection == 9:
                    selection = 11
                elif selection == 10:
                    selection = 10
                elif selection == 11:
                    selection = 9
                elif selection == 12:
                    selection = 8
                elif selection == 13:
                    selection = 7

            # sets the number of stones in selected cup
            num_stones = combined_cups[selection-1][3]
            if num_stones == "0":
                print("The selected cup is empty. Choose another cup")
                continue
            combined_cups[selection - 1][3] = "0"
            top_cups = combined_cups[:6]
            bottom_cups = combined_cups[6:13]
            distribute_stones(combined_cups, distribute_cup, int(num_stones))
            track_points(player_1, player_2)
            draw_board(top_cups, bottom_cups, mancala_a, mancala_b)
            detect_win(combined_cups, player_1, player_2)

            if selection == "quit":  # allows the user to quit the game
                break
        elif players_turn == player_2:
            selection = int(
                input(f"It is {players_turn}'s turn. Enter a cup (1-13) "))
            distribute_cup = selection
            # user must input a number within this range
            if not ((1 <= selection <= 6) or (8 <= selection <= 13)):
                continue
            if selection >= 7:
                if selection == 7:
                    selection = 13
                elif selection == 8:
                    selection = 12
                elif selection == 9:
                    selection = 11
                elif selection == 10:
                    selection = 10
                elif selection == 11:
                    selection = 9
                elif selection == 12:
                    selection = 8
                elif selection == 13:
                    selection = 7

            num_stones = combined_cups[selection-1][3]
            if num_stones == "0":
                print("The selected cup is empty. Choose another cup")
                continue
            # sets the number of stones in selected cup to zero
            combined_cups[selection - 1][3] = "0"
            top_cups = combined_cups[:6]
            bottom_cups = combined_cups[6:13]
            # calls these functions to update the board
            distribute_stones(combined_cups, distribute_cup, int(num_stones))
            track_points(player_1, player_2)
            draw_board(top_cups, bottom_cups, mancala_a, mancala_b)
            detect_win(combined_cups, player_1, player_2)

            if selection == "quit":
                break
        # switches between the two players code
        players_turn = player[1] if players_turn == player[0] else player[0]
    pass


if __name__ == "__main__":
    run_game(game_over)
