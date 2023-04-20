class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        return self.__coinChange(coins, amount, 0)

    def __coinChange(self, coins, amount, count):
        if amount < 0:
            return -1
        if amount == 0:
            return count
        counts = []
        for coin in coins:
            counts.append(self.__coinChange(coins, amount - coin, count + 1))
        retVal = min([count for count in counts if count > 0] or [-1])
        return retVal
