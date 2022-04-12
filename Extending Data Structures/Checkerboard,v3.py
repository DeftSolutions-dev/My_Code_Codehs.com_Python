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

# Your code here...
gg=[]
for i in range(8):
    gg.append([0]*8)
for k in range(8):
    for j in range(8):
        if(k+j)%2==1 and(k<3 or k>4):
            gg[k][j]=1
print_board(gg)