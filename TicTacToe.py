def create_board(n):
    return [[[''] for _ in range(n)] for _ in range(n)]

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
        
    

board = create_board(3)

display_board(board)


def update_board(board, move, player_icon):
    if board[move[0]-1][move[1]-1][0] != '':
        print('Invalid move. That space is full')
        return board
    else:
        board[move[0]-1][move[1]-1] = player_icon
        return board


new_board = update_board(board, [1,1], 'X')

display_board(new_board)