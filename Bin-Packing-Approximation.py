# ---------------------------------------------------------
# Experiment 9
# Efficient Bin Packing using Approximation Algorithms
# ---------------------------------------------------------


# ---------------------------------------------------------
# First Fit (FF)
# ---------------------------------------------------------
def first_fit(items, capacity=1.0):

    bins = []

    for item in items:

        placed = False

        # Try existing bins from left to right
        for i in range(len(bins)):

            if sum(bins[i]) + item <= capacity:
                bins[i].append(item)
                placed = True
                break

        # If item cannot fit in any existing bin
        if not placed:
            bins.append([item])

    return bins


# ---------------------------------------------------------
# First Fit Decreasing (FFD)
# ---------------------------------------------------------
def first_fit_decreasing(items, capacity=1.0):

    # Sort items from largest to smallest
    sorted_items = sorted(items, reverse=True)

    # Apply First Fit
    return first_fit(sorted_items, capacity)


# ---------------------------------------------------------
# Best Fit Decreasing (BFD)
# ---------------------------------------------------------
def best_fit_decreasing(items, capacity=1.0):

    # Sort items from largest to smallest
    sorted_items = sorted(items, reverse=True)

    bins = []

    for item in sorted_items:

        best_bin = -1
        minimum_remaining_space = capacity + 1

        # Find the bin where the item fits
        # with the least remaining space
        for i in range(len(bins)):

            used = sum(bins[i])
            remaining = capacity - used

            if item <= remaining:

                remaining_after = remaining - item

                if remaining_after < minimum_remaining_space:
                    minimum_remaining_space = remaining_after
                    best_bin = i

        # Put item into the best bin
        if best_bin != -1:
            bins[best_bin].append(item)

        # Otherwise create a new bin
        else:
            bins.append([item])

    return bins


# ---------------------------------------------------------
# Display the bins
# ---------------------------------------------------------
def display_bins(name, bins):

    print(f"\n{name}: {len(bins)} bins")

    for i, b in enumerate(bins, 1):

        used = sum(b)

        print(
            f"Bin {i}: "
            f"{[round(x, 1) for x in b]} "
            f"| Used = {used:.1f}"
        )


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------
if __name__ == "__main__":

    # Given items
    items = [
        0.5, 0.7, 0.3, 0.9, 0.2,
        0.6, 0.8, 0.4, 0.1, 0.5
    ]

    capacity = 1.0

    # Theoretical lower bound
    lower_bound = int(sum(items) / capacity)

    if sum(items) % capacity != 0:
        lower_bound += 1

    print("Efficient Bin Packing using Approximation Algorithms")
    print("=" * 60)

    print("\nItems:")
    print(items)

    print(f"\nBin Capacity: {capacity}")

    print(f"Total size: {sum(items):.1f}")

    print(f"Theoretical Lower Bound: {lower_bound}")

    # Run algorithms
    ff_bins = first_fit(items, capacity)

    ffd_bins = first_fit_decreasing(items, capacity)

    bfd_bins = best_fit_decreasing(items, capacity)

    # Display results
    display_bins("First Fit (FF)", ff_bins)

    display_bins("First Fit Decreasing (FFD)", ffd_bins)

    display_bins("Best Fit Decreasing (BFD)", bfd_bins)

    # Final comparison
    print("\n" + "=" * 60)
    print("FINAL COMPARISON")
    print("=" * 60)

    print(f"Lower Bound : {lower_bound} bins")
    print(f"First Fit   : {len(ff_bins)} bins")
    print(f"FFD         : {len(ffd_bins)} bins")
    print(f"BFD         : {len(bfd_bins)} bins")