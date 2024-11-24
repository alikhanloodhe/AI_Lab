def solve_n_queens_arc_consistency(N):
    from collections import deque

    # Initialize domains: each row can use any column initially
    domains = {}
    for r in range(N):
      domains[r] = set(range(N))

    # Function to enforce arc consistency using AC-3
    def ac3():
        # Initialize the queue with all arcs (row pairs)
        queue = deque()
        for X in range(N):
            for Y in range(N):
                if X != Y:
                    queue.append((X, Y))

        while queue:
            X, Y = queue.popleft()

            # Revise the domain of X
            if revise(X, Y):
                # If a domain becomes empty, return False (unsolvable)
                if not domains[X]:
                    return False
                # Add related arcs back to the queue
                for Z in range(N):
                    if Z != X and Z != Y:
                        queue.append((Z, X))
        return True

    # Revise the domain of X based on Y
    def revise(X, Y):
        revised = False
        to_remove = set()

        for x in domains[X]:
            # Check if there exists a valid y in Y's domain
            if not any(is_consistent(x, y, X, Y) for y in domains[Y]):
                to_remove.add(x)
                
                revised = True

        # Remove inconsistent values from X's domain
        domains[X] -= to_remove
        return revised

    # Check if placing queens at (row X, col x) and (row Y, col y) is consistent
    def is_consistent(x, y, X, Y):
        return x != y and abs(x - y) != abs(X - Y)

    # Backtracking function to find all solutions
    def backtrack(row, current_solution):
        if row == N:  # All queens are placed
            solution_grid = []
            for r in range(N):
                solution_grid.append("".join("Q" if c in domains[r] else "." for c in range(N)))
            solutions_grid.append(solution_grid)
            solutions_numeric.append(current_solution[:])
            return

        # Try placing a queen in each valid column
        original_domains = {r: set(domains[r]) for r in range(N)}
        for col in domains[row]:
            # Place queen and update domains
            domains[row] = {col}
            current_solution.append(col)

            # Propagate constraints to future rows using AC-3
            if ac3():
                backtrack(row + 1, current_solution)

            # Restore original domains (backtrack)
            domains.update({r: set(original_domains[r]) for r in range(N)})
            current_solution.pop()

    solutions_grid = []   # Board representation solutions
    solutions_numeric = []  # Numerical solutions
    backtrack(0, [])
    return solutions_grid, solutions_numeric



solutions_grid, solutions_numeric = solve_n_queens_arc_consistency(4)

print("Grid-based solutions:")
for solution in solutions_grid:
    for row in solution:
        print(row)
    print()

print("Numerical solutions:")
for solution in solutions_numeric:
    print(solution)
