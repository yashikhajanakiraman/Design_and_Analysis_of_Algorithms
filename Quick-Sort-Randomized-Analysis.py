# ---------------------------------------------------------
# Experiment 10
# Improving Quick Sort Efficiency using Randomized Algorithm
# ---------------------------------------------------------

import random
import time
import sys

# Allow deeper recursion for Quick Sort
sys.setrecursionlimit(20000)

comparisons = 0


# ---------------------------------------------------------
# Partition
# ---------------------------------------------------------
def partition(arr, low, high):

    global comparisons

    # Last element is used as pivot
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        comparisons += 1

        if arr[j] <= pivot:

            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# ---------------------------------------------------------
# Deterministic Quick Sort
# Pivot = Last Element
# ---------------------------------------------------------
def deterministic_quicksort(arr, low, high):

    if low < high:

        pi = partition(arr, low, high)

        deterministic_quicksort(arr, low, pi - 1)

        deterministic_quicksort(arr, pi + 1, high)


# ---------------------------------------------------------
# Randomized Quick Sort
# Pivot = Random Element
# ---------------------------------------------------------
def randomized_quicksort(arr, low, high):

    if low < high:

        # Select a random pivot
        rand_idx = random.randint(low, high)

        # Move random pivot to the last position
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

        # Partition
        pi = partition(arr, low, high)

        randomized_quicksort(arr, low, pi - 1)

        randomized_quicksort(arr, pi + 1, high)


# ---------------------------------------------------------
# Run a test and measure performance
# ---------------------------------------------------------
def run_test(sort_fn, arr):

    global comparisons

    # Make a copy so original input is not modified
    a = arr[:]

    comparisons = 0

    start = time.perf_counter()

    sort_fn(a, 0, len(a) - 1)

    elapsed = (time.perf_counter() - start) * 1000

    return comparisons, elapsed


# ---------------------------------------------------------
# Generate Test Cases
# ---------------------------------------------------------

N = 5000

test_cases = {

    # Random input
    "Random":
        [random.randint(1, 100000) for _ in range(N)],

    # Already sorted
    "Sorted":
        list(range(N)),

    # Reverse sorted
    "Reverse":
        list(range(N, 0, -1)),

    # Nearly sorted
    "Nearly Sorted":
        list(range(N))
}


# ---------------------------------------------------------
# Make Nearly Sorted input
# ---------------------------------------------------------

ns = test_cases["Nearly Sorted"]

for _ in range(N // 20):

    i = random.randint(0, N - 1)

    j = random.randint(0, N - 1)

    ns[i], ns[j] = ns[j], ns[i]


# ---------------------------------------------------------
# Display Header
# ---------------------------------------------------------

print(
    f"{'Input Type':<16}"
    f"{'DQS Comps':>12}"
    f"{'DQS Time(ms)':>14}"
    f"{'RQS Comps':>12}"
    f"{'RQS Time(ms)':>14}"
)

print("-" * 68)


# ---------------------------------------------------------
# Run all test cases
# ---------------------------------------------------------

for case, arr in test_cases.items():

    d_comps, d_time = run_test(
        deterministic_quicksort,
        arr
    )

    r_comps, r_time = run_test(
        randomized_quicksort,
        arr
    )

    print(
        f"{case:<16}"
        f"{d_comps:>12}"
        f"{d_time:>14.2f}"
        f"{r_comps:>12}"
        f"{r_time:>14.2f}"
    )