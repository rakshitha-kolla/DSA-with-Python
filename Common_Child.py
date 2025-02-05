def common_child(s1, s2):
    # Create a 2D list to store the lengths of LCS
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of the longest common subsequence is stored in dp[n][m]
    return dp[n][m]

# Input strings
s1 = input("Enter String1: ")
s2 = input("Enter String2: ")

# Compute and print the result
result = common_child(s1, s2)
print("The length of the longest common subsequence is:", result)
