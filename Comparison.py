from N_Queen_Arc_consistancy import solve_n_queens_arc_consistency
from nQueenBacktracking import solve_n_queens_backtracking
from nQueenForwardCheck import solve_n_queens_forward_checking
import time
import matplotlib.pyplot as plt

def compare_algorithms(N_values):
    algorithms = {
        "Backtracking": solve_n_queens_backtracking,
        "Forward Checking": solve_n_queens_forward_checking,
        "Arc Consistency": solve_n_queens_arc_consistency,
    }

    results = []
    for N in N_values:
        print(f"Running comparisons for N = {N}...")
        for name, solver in algorithms.items():
            recursive_call_count = {"count": 0}

            # Adjust solver to count recursive calls
            def solver_with_count(*args, **kwargs):
                nonlocal recursive_call_count
                recursive_call_count["count"] += 1
                return solver(*args, **kwargs)

            start_time = time.time()
            solutions = solver_with_count(N)  # Ensure solvers return solutions
            end_time = time.time()

            results.append({
                "Algorithm": name,
                "N": N,
                "Execution Time": end_time - start_time,
                "Recursive Calls": recursive_call_count["count"],
                "Solution Count": len(solutions),
            })
    return results

def plot_results(results):
    algorithms = list(set(r["Algorithm"] for r in results))
    N_values = sorted(set(r["N"] for r in results))

    execution_times = {algo: [] for algo in algorithms}
    recursive_calls = {algo: [] for algo in algorithms}
    solution_counts = {algo: [] for algo in algorithms}

    for algo in algorithms:
        for N in N_values:
            for result in results:
                if result["Algorithm"] == algo and result["N"] == N:
                    execution_times[algo].append(result["Execution Time"])
                    recursive_calls[algo].append(result["Recursive Calls"])
                    solution_counts[algo].append(result["Solution Count"])

    plt.figure(figsize=(12, 6))
    for algo in algorithms:
        plt.plot(N_values, execution_times[algo], marker="o", label=f"{algo} (Execution Time)")
    plt.xlabel("N (Board Size)")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(12, 6))
    for algo in algorithms:
        plt.plot(N_values, recursive_calls[algo], marker="o", label=f"{algo} (Recursive Calls)")
    plt.xlabel("N (Board Size)")
    plt.ylabel("Recursive Calls")
    plt.title("Recursive Calls Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()

N_values = [4, 8, 12]
results = compare_algorithms(N_values)

print(f"{'Algorithm':<20}{'N':<5}{'Time (s)':<15}{'Recursive Calls':<15}{'Solutions':<10}")
for result in results:
    print(f"{result['Algorithm']:<20}{result['N']:<5}{result['Execution Time']:<15.6f}{result['Recursive Calls']:<15}{result['Solution Count']:<10}")

plot_results(results)
