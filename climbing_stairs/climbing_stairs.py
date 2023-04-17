class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {i: -1 for i in range(n + 1)}
        return self.__climbStairs(n, dp)

    def __climbStairs(self, n: int, dp: dict) -> int:
        if n <= 2:
            return n
        if dp[n - 1] < 0:
            dp[n - 1] = self.__climbStairs(n - 1, dp)
        if dp[n - 2] < 0:
            dp[n - 2] = self.__climbStairs(n - 2, dp)
        return dp[n - 1] + dp[n - 2]
