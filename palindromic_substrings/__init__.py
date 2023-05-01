class Solution:
    def countSubstrings(self, s: str) -> int:
        ct = 0
        memo: set = {}
        for i in range(len(s)):
            ct += self.__countSubstrings(s, i, i, memo)
            ct += self.__countSubstrings(s, i, i + 1, memo)
        return ct

    def __countSubstrings(self, s: str, left, right, memo: set):
        if (left, right) not in memo:
            if left < 0 or right >= len(s) or s[left] != s[right]:
                memo[(left, right)] = 0
            else:
                memo[(left, right)] = 1 + self.__countSubstrings(
                    s, left - 1, right + 1, memo
                )
        return memo[(left, right)]
