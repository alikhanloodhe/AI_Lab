



def solve_n_queens_forward_checking(N):
    # Initialize an empty board and the list of solutions
    board = [["."] * N for _ in range(N)]
    solutions = []

    # Initialize valid columns for each row
    valid_columns = [set(range(N)) for _ in range(N)]

    def is_valid_to_place(row, col):
        # Check if the current column and diagonals are valid
        for r in range(row):
            if board[r][col] == "Q" or \
               col - (row - r) >= 0 and board[r][col - (row - r)] == "Q" or \
               col + (row - r) < N and board[r][col + (row - r)] == "Q":
                return False
        return True

    def forward_check(row):
        if row == N:
            # Add current valid board configuration to solutions
            solutions.append(["".join(row) for row in board])
            return True

        for col in list(valid_columns[row]):
            if is_valid_to_place(row, col):
                # Place the queen and update the board
                board[row][col] = "Q"

                # Update the valid columns for the next rows
                updated_columns = [set(cols) for cols in valid_columns]
                for r in range(row + 1, N):
                    updated_columns[r].discard(col)
                    updated_columns[r].discard(col - (r - row))
                    updated_columns[r].discard(col + (r - row))

                    # If any future row has no valid columns, backtrack
                    if not updated_columns[r]:
                        board[row][col] = "."
                        break
                else:
                    # Recursively call forward_check for the next row
                    valid_columns[row] = updated_columns[row]
                    if forward_check(row + 1):
                        board[row][col] = "."
                        continue

                # Remove the queen (backtrack)
                board[row][col] = "."

        return False

    forward_check(0)
    return solutions


# solutions = solve_n_queens_forward_checking(4)
# for solution in solutions:
#     for row in solution:
#         print(row)
#     print()
