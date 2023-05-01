class Solution:
    def countSubstrings(self, s: str) -> int:
        ct = 0
        for i in range(len(s)):
            ct += self.__countSubstrings(s, i, i)
            ct += self.__countSubstrings(s, i, i + 1)
        return ct

    def __countSubstrings(self, s: str, left, right):
        if left < 0 or right >= len(s) or s[left] != s[right]:
            return 0
        return 1 + self.__countSubstrings(s, left - 1, right + 1)
