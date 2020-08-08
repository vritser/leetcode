# https://leetcode.com/problems/guess-number-higher-or-lower-ii/
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[float('inf')] * (n + 1) for _ in range(n +1)]

        for i in reversed(range(1, n + 1)):
            for j in range(i, n + 1):
                if i == j:
                    dp[i][j] = 0
                elif j - i == 1:
                    dp[i][j] = i
                else:
                    for k in range(i+1, j):
                        dp[i][j] = min(dp[i][j], max(dp[i][k-1] + k, dp[k+1][j] + k))

        return dp[1][n]
