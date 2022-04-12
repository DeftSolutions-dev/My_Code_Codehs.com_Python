# Pass this function a list of lists, and it will
# print it such that it looks like the grids in
# the exercise instructions.
def print_board(board):
    for i in range(len(board)):
        
        # This line uses some Python you haven't
        # learned yet. You'll learn about this
        # part in a future lesson:
        #
        # [str(x) for x in board[i]]
        print(" ".join([str(x) for x in board[i]]))

gg=[]
for p in range(8):
    gg.append([0]*8)
    for m in range(8):
        for f in range(8):
            if p<3 or p>4:
                gg[p][f]=1
print_board(gg)