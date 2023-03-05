n=4
board=[[0 for _ in range(n) ] for _ in range(n)]
def isattack(i,j):
    for k in range(n):
        if(board[i][k]==1 or board[k][j]==1):
            return True
    for k in range(n):
        for l in range(n):
            if (k+l==i+j or k-l==i-j):
                if board[k][j]==1:
                    return True
    return False
def nQueens(n):
    if n==0:
        return True
    for i in range(0,n):
        for j in range(0,n):
            if not(isattack(i,j)) and board[i][j]!=1:
                board[i][j] =1
                if nQueens(n-1):
                    return True
