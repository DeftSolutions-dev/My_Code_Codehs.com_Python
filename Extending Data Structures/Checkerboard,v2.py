# Pass this function a list of lists, and it will
# print it such that it looks like the grids in
# the exercise instructions.
def print_board(board):
    for i in range(len(board)):
        
        # This line uses some Python you haven't
        # learned yet. You'll learn about this
        # part in a future lesson
        #
        # [str(x) for x in board[i]]
        print(" ".join([str(x) for x in board[i]]))

board=[]
for i in range(8):
    if i % 2==0:
        board.append([0,1]*4)
    else:
        board.append([1,0]*4)
        board[1][2]=1
print_board(board)