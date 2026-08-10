# ---------------------------------------------------------
# Travelling Salesman Problem using Branch and Bound
# ---------------------------------------------------------

INF = float('inf')


# ---------------------------------------------------------
# Calculate the initial lower bound
# ---------------------------------------------------------
def calculate_bound(cost, visited):

    n = len(cost)
    bound = 0

    for i in range(n):

        if visited[i]:
            continue

        # Find the two smallest outgoing edges
        edges = []

        for j in range(n):
            if i != j and not visited[j]:
                edges.append(cost[i][j])

        if i == 0:
            # Include edges from the starting city
            for j in range(n):
                if j != i:
                    edges.append(cost[i][j])

        if len(edges) >= 2:
            edges.sort()
            bound += edges[0] + edges[1]
        elif len(edges) == 1:
            bound += edges[0]

    return bound / 2


# ---------------------------------------------------------
# Branch and Bound TSP
# ---------------------------------------------------------
def tsp_branch_and_bound(cost):

    n = len(cost)

    visited = [False] * n
    visited[0] = True

    best_cost = [INF]
    best_path = []

    current_path = [0]

    def branch(current, current_cost):

        # If all cities are visited
        if len(current_path) == n:

            return_cost = cost[current][0]
            total_cost = current_cost + return_cost

            if total_cost < best_cost[0]:

                best_cost[0] = total_cost
                best_path.clear()
                best_path.extend(current_path)
                best_path.append(0)

            return

        # Try every unvisited city
        for next_city in range(n):

            if visited[next_city]:
                continue

            new_cost = current_cost + cost[current][next_city]

            # Simple lower-bound estimate
            lower_bound = new_cost

            if lower_bound >= best_cost[0]:
                continue

            # Choose this city
            visited[next_city] = True
            current_path.append(next_city)

            branch(next_city, new_cost)

            # Backtrack
            current_path.pop()
            visited[next_city] = False

    branch(0, 0)

    return best_path, best_cost[0]


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------
if __name__ == "__main__":

    # Cost matrix
    cost = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    path, minimum_cost = tsp_branch_and_bound(cost)

    print("Travelling Salesman Problem")
    print("=" * 40)

    print("\nCost Matrix:")

    for row in cost:
        print(row)

    print("\nOptimal Tour:")

    print(" -> ".join(map(str, path)))

    print(f"\nMinimum Tour Cost: {minimum_cost}")