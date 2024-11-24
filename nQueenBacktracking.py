def solve_n_queens_backtracking(N):
    col = set()
    posDiag = set()  # r + c (positive slope diagonals)
    negDiag = set()  # r - c (negative slope diagonals)
    
    board = [["."] * N for _ in range(N)]
    solutions = []

    def backtrack(r):
        if r == N:
            copy = ["".join(row) for row in board]
            solutions.append(copy)
            return

        for c in range(N):
            if c in col or (r + c) in posDiag or (r - c) in negDiag: #Checking if the position is correct or not
                continue

            # Place the queen
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            # Recurse to the next row
            backtrack(r + 1)

            # Remove the queen (backtrack)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return solutions


# solutions = solve_n_queens_backtracking(4)
# for solution in solutions:
#     for row in solution:
#         print(row)
#     print()
