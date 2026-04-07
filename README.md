# Assignment 3 — Highest Value Longest Common Subsequence (HVLCS)

## Student Info
- **Name:** Sebastian Robalino-Ordoñez
- **UFID:** 8415-9795

## Description
This program computes the highest-value common subsequence of two strings, where each character has an assigned value.

## How to Build
No compilation needed — Python 3.

## How to Run

```bash
python3 src/hvlcs.py < data/example.in
```

## Example

Input file `data/example.in`:
```
4
a 2
b 4
c 5
d 0
aacb
caab
```

Output (also in `data/example.out`):
```
9
cb
```

## Assumptions
- Input is well-formed and follows the specified format.
- Character values are nonnegative integers.
- Python 3.8+ is required.
- No external libraries needed for the core solver. `matplotlib` is needed only for generating the graph.

---

## Question 1: Empirical Comparison

See `data/runtime_graph.png` for the runtime graph.

10 test inputs with string lengths from 25 to 750 were used. The graph plots input size (m * n) vs. runtime in seconds, confirming the expected O(m*n) growth.

## Question 2: Recurrence Equation

Let A = a1 a2 ... am and B = b1 b2 ... bn.

Define dp[i][j] = maximum value of a common subsequence of A[1..i] and B[1..j].

**Base cases:**

```
dp[0][j] = 0   for all j = 0..n
dp[i][0] = 0   for all i = 0..m
```

**Recurrence (for i >= 1, j >= 1):**

```
If A[i] == B[j]:
    dp[i][j] = dp[i-1][j-1] + value(A[i])
Else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

**Why this is correct:**

- If A[i] == B[j], we can extend the best subsequence of A[1..i-1] and B[1..j-1] by appending this matching character, adding its value.
- If A[i] != B[j], at least one of them is not in the optimal subsequence, so we take the better of skipping either.
- Base cases: an empty prefix has no common subsequence, so the value is 0.

This generalizes standard LCS by replacing "+1 for length" with "+value(character)".

## Question 3: Big-O and Pseudocode

**Pseudocode:**

```
HVLCS(A, B, value):
    m = length(A)
    n = length(B)
    Create dp[0..m][0..n], initialize all to 0

    for i = 1 to m:
        for j = 1 to n:
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + value(A[i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

**Runtime: O(m * n)** where m = |A| and n = |B|.

- The DP table has (m+1)(n+1) cells, each computed in O(1).
- Reconstruction (backtracking) is O(m + n).
- Total: **O(m * n)**.