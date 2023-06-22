def solveKT(n, start_x, start_y):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def is_valid(x, y, board):
        if x >= 0 and x < n and y >= 0 and y < n and board[x][y] == -1:
            return True
        return False

    def solveKTUtil(x, y, movei, board, memo):
        if movei == n**2:
            return True
        if memo[x][y] != -1:
            return memo[x][y]
        for i in range(8):
            next_x = x + moves[i][0]
            next_y = y + moves[i][1]
            if is_valid(next_x, next_y, board):
                board[next_x][next_y] = movei
                if solveKTUtil(next_x, next_y, movei+1, board, memo):
                    memo[x][y] = True
                    return True
                board[next_x][next_y] = -1
        memo[x][y] = False
        return False

    board = [[-1 for i in range(n)] for j in range(n)]
    memo = [[-1 for i in range(n)] for j in range(n)]
    board[start_x][start_y] = 0
    if solveKTUtil(start_x, start_y, 1, board, memo):
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()
    else:
        print("Solution does not exist")

# Example usage with starting position (2, 3) on a 6x6 chessboard
solveKT(6, 2, 3)
