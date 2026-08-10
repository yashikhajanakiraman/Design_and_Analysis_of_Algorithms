import time
import random
import string


# ---------------------------------------------------------
# Naive String Matching
# ---------------------------------------------------------
def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


# ---------------------------------------------------------
# Compute LPS Array for KMP
# ---------------------------------------------------------
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps


# ---------------------------------------------------------
# KMP String Matching
# ---------------------------------------------------------
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:

        comparisons += 1

        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:

            if j != 0:
                j = lps[j - 1]

            else:
                i += 1

    return matches, comparisons


# ---------------------------------------------------------
# Rabin-Karp String Matching
# ---------------------------------------------------------
def rabin_karp(text, pattern, q=101):

    n, m = len(text), len(pattern)

    d = 256

    # h = d^(m-1) mod q
    h = pow(d, m - 1, q)

    p_hash = 0
    t_hash = 0

    matches = []
    comparisons = 0

    # Calculate initial hash values
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Slide the pattern over the text
    for s in range(n - m + 1):

        # Hash values match
        if p_hash == t_hash:

            # Verify character by character
            for k in range(m):

                comparisons += 1

                if text[s + k] != pattern[k]:
                    break

            else:
                matches.append(s)

        # Calculate hash for next window
        if s < n - m:

            t_hash = (
                d * (t_hash - ord(text[s]) * h)
                + ord(text[s + m])
            ) % q

            if t_hash < 0:
                t_hash += q

    return matches, comparisons


# ---------------------------------------------------------
# Main Execution
# ---------------------------------------------------------
if __name__ == "__main__":

    # Sample text and pattern
    text = "AABAACAADAABAABA"
    pattern = "AABA"

    print("Text:", text)
    print("Pattern:", pattern)

    # Naive
    m1, c1 = naive_search(text, pattern)

    # KMP
    m2, c2 = kmp_search(text, pattern)

    # Rabin-Karp
    m3, c3 = rabin_karp(text, pattern)

    print(f"\nNaive -> Matches at: {m1}, Comparisons: {c1}")
    print(f"KMP -> Matches at: {m2}, Comparisons: {c2}")
    print(f"RK -> Matches at: {m3}, Comparisons: {c3}")


    # -----------------------------------------------------
    # Performance Comparison
    # -----------------------------------------------------

    # Generate a random text of 10,000 characters
    text_large = ''.join(
        random.choices("ABCD", k=10000)
    )

    # Patterns of varying lengths
    patterns = [
        "AB",
        "ABCD",
        "ABCDAB",
        "ABCDABCD"
    ]

    print(
        f'\n{"Pattern":>12} '
        f'{"Naive":>10} '
        f'{"KMP":>10} '
        f'{"RK":>10}'
    )

    print("-" * 50)

    for p in patterns:

        _, c1 = naive_search(text_large, p)
        _, c2 = kmp_search(text_large, p)
        _, c3 = rabin_karp(text_large, p)

        print(
            f'{p:>12} '
            f'{c1:>10} '
            f'{c2:>10} '
            f'{c3:>10}'
        )