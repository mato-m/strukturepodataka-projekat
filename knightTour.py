def solveKT(n):
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
        memo[x][y] = -1
        return False

    board = [[-1 for _ in range(n)] for _ in range(n)]
    memo = [[-1 for _ in range(n)] for _ in range(n)]  # Memoization table

    print("Enter the starting position (row, column):")
    start_row = int(input("Row: "))
    start_col = int(input("Column: "))

    if start_row < 0 or start_row >= n or start_col < 0 or start_col >= n:
        print("Invalid starting position.")
        return

    board[start_row][start_col] = 0

    if solveKTUtil(start_row, start_col, 1, board, memo):
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()
    else:
        print("Solution does not exist")


solveKT(6)
