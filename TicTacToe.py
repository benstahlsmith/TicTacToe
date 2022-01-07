import random as rd

def create_board(n):
    return [[' ' for _ in range(n)] for _ in range(n)]

def display_board(board):
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
            print('_____')
            i += 1
        
gameboard = create_board(3)

def update_board(board, player_icon):
    while 1 == 1:
        move = [int(input('Choose row: '))]
        move.append(int(input('Choose column: ')))
        if board[move[0]-1][move[1]-1] != ' ':
            print('Invalid move. That space is full. Please try again.')
        else:
            board[move[0]-1][move[1]-1] = player_icon
            return board

def check_for_winner(board):
    # print(board)
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
    n = len(board)
    while 1==1:
        move = [rd.randint(0,n-1), rd.randint(0,n-1)]
        if board[move[0]][move[1]] == ' ':
            board[move[0]][move[1]] = player_icon
            return board
            

def one_player_game(n, player):
    board = create_board(n)
    display_board(board)
    player1_icon = 'X'
    computer_icon = 'O'
    while 1 == 1:
        board = update_board(board, player1_icon)
        display_board(board)
        if check_for_winner(board):
            return player
        board = fill_random_space(board, computer_icon)
        display_board(board)
        if check_for_winner(board):
            return 'Computer'


winner = one_player_game(3, 'Ben')

print(winner)


# def main():
#     n = input("What board size do you want to use? ")
#     player1 = input("Player 1 name: ")
#     # player1_icon = input("Player 1 icon: ")
#     while 1 == 1:
#         player2 = input("Player 2 name (Enter nothing for 1 player game): ")
#         if player2 == player1:
#             print("That name has already been used.")
#         else:
#             break
#     if player2 == '':
#         one_player_game(n, player1)
