def solveKT(n):

    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def is_valid(x, y, board):
        if x >= 0 and x < n and y >= 0 and y < n and board[x][y] == -1:
            return True
        return False
    
    def solveKTUtil(x, y, movei, board):
        if movei == n**2:
            return True
        for i in range(8):
            next_x = x + moves[i][0]
            next_y = y + moves[i][1]
            if is_valid(next_x, next_y, board):
                board[next_x][next_y] = movei
                if solveKTUtil(next_x, next_y, movei+1, board):
                    return True
                board[next_x][next_y] = -1
        return False
       # Initialize the board with -1's
    board = [[-1 for i in range(n)] for j in range(n)]
    # Start from the top-left corner of the board
    board[0][0] = 0
    # Solve the problem recursively
    if solveKTUtil(0, 0, 1, board):
        # Print the solution
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()
    else:
        print("Solution does not exist")

solveKT(6)
