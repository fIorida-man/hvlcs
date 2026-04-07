import sys


def solve():
    data = sys.stdin.read().split('\n')
    idx = 0

    k = int(data[idx]); idx += 1

    value = {}
    for _ in range(k):
        parts = data[idx].split(); idx += 1
        char = parts[0]
        val = int(parts[1])
        value[char] = val

    A = data[idx].strip(); idx += 1
    B = data[idx].strip(); idx += 1

    m = len(A)
    n = len(B)

    # Build DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + value.get(A[i - 1], 0)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the subsequence
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            result.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()

    print(dp[m][n])
    print(''.join(result))


if __name__ == '__main__':
    solve()