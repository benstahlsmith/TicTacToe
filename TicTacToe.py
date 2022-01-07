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

display_board(gameboard)

print(gameboard)
def update_board(board, move, player_icon):
    if board[move[0]-1][move[1]-1] != ' ':
        print('Invalid move. That space is full')
        return board
    else:
        board[move[0]-1][move[1]-1] = player_icon
        return board


new_board = update_board(gameboard, [1,1], 'X')


display_board(new_board)

print(new_board)

def check_for_winner(board):
    print(board)
    n = len(board)
    for row in board:
        for i in range(1,n):
            if row[i] == row[i-1]:
                if i == n - 1:
                    print(row[i] + ' is the winner')
                    return True
                i += 1
                continue
            else:
                break

check_for_winner(new_board)

new_board = update_board(new_board, [1,2], 'X')
new_board = update_board(new_board, [1,3], 'X')

display_board(new_board)

check_for_winner(new_board)