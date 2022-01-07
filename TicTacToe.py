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

def update_board(board, move, player_icon):
    if board[move[0]-1][move[1]-1] != ' ':
        print('Invalid move. That space is full')
        return board
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
                    print(current + ' is the winner')
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
                    print(current + ' is the winner')
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
                print(current + ' is the winner')
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
                print(current + ' is the winner')
                return True
            continue
        else:
            break


def fill_random_space(board, player_icon):
    n = len(board)
    while 1==1:
        move = [rd.randint(0,n-1), rd.randint(0,n-1)]
        if board[move[0]][move[1]] == ' ':
            board[move[0]][move[1]] = player_icon
            return board
            



new_board = update_board(gameboard, [1,3], 'X')
new_board = update_board(new_board, [2,2], 'X')
new_board = update_board(new_board, [2,1], 'X')
new_board = fill_random_space(new_board, 'O')

display_board(new_board)

# check_for_winner(new_board)
