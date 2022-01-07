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
        
    

board = [[['X'], ['X'], ['X']], [['X'], ['X'], ['X']], [['X'], ['X'], ['X']]]

display_board(board)