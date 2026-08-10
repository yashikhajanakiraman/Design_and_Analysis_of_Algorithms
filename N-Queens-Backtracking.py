# ---------------------------------------------------------
# N-Queens Problem using Backtracking
# ---------------------------------------------------------


# ---------------------------------------------------------
# Check whether a queen can be placed safely
# ---------------------------------------------------------
def is_safe(board, row, col):

    for prev_row in range(row):

        placed = board[prev_row]

        # Same column
        if placed == col:
            return False

        # Same diagonal
        if abs(prev_row - row) == abs(placed - col):
            return False

    return True


# ---------------------------------------------------------
# Solve N-Queens using Backtracking
# ---------------------------------------------------------
def solve_n_queens(n):

    board = [-1] * n
    solutions = []

    # Mutable counter so it can be updated inside recursion
    backtrack_count = [0]

    def backtrack(row):

        # All queens have been placed
        if row == n:
            solutions.append(board[:])
            return

        # Try every column
        for col in range(n):

            if is_safe(board, row, col):

                # Place queen
                board[row] = col

                # Move to next row
                backtrack(row + 1)

                # Undo placement
                board[row] = -1

                # Count the backtrack
                backtrack_count[0] += 1

    backtrack(0)

    return solutions, backtrack_count[0]


# ---------------------------------------------------------
# Display Chessboard
# ---------------------------------------------------------
def display_board(solution, n):

    print(" +" + "---+" * n)

    for row in range(n):

        print(" |", end="")

        for col in range(n):

            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")

        print()
        print(" +" + "---+" * n)


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------
if __name__ == "__main__":

    # Solve for N = 4, 6 and 8
    for n in [4, 6, 8]:

        solutions, backtracks = solve_n_queens(n)

        print(
            f"N={n}: "
            f"{len(solutions)} solutions, "
            f"{backtracks} backtracks"
        )

        # Display all solutions only for N=4
        if n == 4:

            print(f"\nAll solutions for {n}-Queens:")

            for i, solution in enumerate(solutions, 1):

                print(f"\nSolution {i}: {solution}")

                display_board(solution, n)

        print()