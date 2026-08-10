class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)

        # dp[row][col] = LCS length for text1[row:] and text2[col:]
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Work backward so dp[row + 1][col] and dp[row][col + 1]
        # are ready when calculating dp[row][col].
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(
                        dp[row + 1][col],
                        dp[row][col + 1],
                    )

        return dp[0][0]