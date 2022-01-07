import random as rd

def create_board(n):
    """
    creates a square game board of any size

    Inputs:
    n - integer

    Outputs:
    board - a list containg lists for each row
    """
    return [[' ' for _ in range(n)] for _ in range(n)]

def display_board(board):
    """
    Displays a board in the console

    Inputs:
    board - game board created or updated by other functions

    Outputs:
    none
    """
    i = 1
    for row in board:
        j = 1
        for entry in row:
            if j != len(row):
                print(entry[0] + '|', end='')
                j += 1
            else:
                print(entry[0])
        if len(board) != i:
            print('_'*(len(board)*2))
            i += 1
        

def update_board(board, player_icon):
    """
    Take in a current board and icon and have the player make a move. Will check to ensure move is valid before placing the icon.

    Inputs:
    board - list of lists created by create_bard
    player_icon - icon of the current player, X or O

    Outputs:
    board - updated board with player move
    """
    while 1 == 1:
        move = [int(input('Choose row: '))]
        move.append(int(input('Choose column: ')))
        if board[move[0]-1][move[1]-1] != ' ':
            print('Invalid move. That space is full. Please try again.')
        else:
            board[move[0]-1][move[1]-1] = player_icon
            return board

def check_for_winner(board):
    """
    Scans the board to see if a player has won

    Inputs:
    board - game board

    Outputs:

    name of the winner
    """
    n = len(board)
    for row in board:
        for i in range(1,n):
            current = row[i]
            prev = row[i-1]
            if current == ' ' or prev == ' ':
                break
            elif current == prev:
                if i == n - 1:
                    return True
                continue
            else:
                break
    
    for i in range(0,n):
        for j in range(1,n):
            current = board[j][i]
            prev = board[j-1][i]
            if current == ' ' or prev == ' ':
                break
            elif current == prev:
                if j == n-1:
                    return True
                continue
            else:
                break

    for i in range(1,n):
        current = board[i][i]
        prev = board[i-1][i-1]
        if current == ' ' or prev == ' ':
                break
        elif current == prev:
            if i == n-1:
                return True
            continue
        else:
            break
    for i in range(1,n):
        current = board[i][n-i-1]
        prev = board[i-1][n-i]
        if current == ' ' or prev == ' ':
                break
        elif current == prev:
            if i == n-1:
                return True
            continue
        else:
            break
    return False


def fill_random_space(board, player_icon):
    """
    Inputs the icon into a random spot on the board. Used for computer players
    Inputs:
    board - game board
    player_icon - icon for the computer

    Outputs:
    updated game board
    """
    n = len(board)
    while 1==1:
        move = [rd.randint(0,n-1), rd.randint(0,n-1)]
        if board[move[0]][move[1]] == ' ':
            board[move[0]][move[1]] = player_icon
            return board
            

def one_player_game(n, player):
    """
    Plays a game with one player against the computer

    Inputs:
    n - size of the game board
    player - name of the player

    Outputs:
    name of the winner
    """
    board = create_board(n)
    display_board(board)
    player1_icon = 'X'
    computer_icon = 'O'
    maxmoves = n*n
    moves = 0
    while moves < maxmoves:
        board = update_board(board, player1_icon)
        display_board(board)
        if check_for_winner(board):
            return player
        moves += 1
        if moves == maxmoves:
            print("No more moves left.")
            return 'No-one'
        board = fill_random_space(board, computer_icon)
        display_board(board)
        if check_for_winner(board):
            return 'Computer'
        moves += 1
    return 'No-one'


def two_player_game(n, player1, player2):
    """
    Plays a game with 2 players

    Inputs:
    n - size of the game board
    player1 - name of the player1
    player2 - name of the player2

    Outputs:
    name of the winner
    """
    board = create_board(n)
    display_board(board)
    player1_icon = 'X'
    player2_icon = 'O'
    maxmoves = n*n
    moves = 0
    while moves < maxmoves:
        print(player1 + "'s move")
        board = update_board(board, player1_icon)
        display_board(board)
        if check_for_winner(board):
            return player1
        moves += 1
        if moves == maxmoves:
            print("No more moves left.")
            return 'No-one'
        print(player2 + "'s move")
        board = update_board(board, player2_icon)
        display_board(board)
        if check_for_winner(board):
            return player2
        moves += 1
    return 'No-one'

def main():
    n = int(input("What board size do you want to use? "))
    player1 = input("Player 1 name: ")
    # player1_icon = input("Player 1 icon: ")
    while 1 == 1:
        player2 = input("Player 2 name (Enter nothing for 1 player game): ")
        if player2 == player1:
            print("That name has already been used.")
        else:
            break
    if player2 == '':
        winner = one_player_game(n, player1)
    else:
        winner = two_player_game(n, player1, player2)
    if winner == 'No-one':
        print("Draw!")
    else:
        print(winner + ' has won the game. Nice Job!')

if __name__ == '__main__':
    main()
