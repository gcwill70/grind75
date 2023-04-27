# create sliding window
# start and end pointers
# increment end


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.__longestPalindrome(s, 0, len(s) - 1)

    def __longestPalindrome(self, s: str, start: int, end: int) -> str:
        if start > end:
            return ""
        if start == end:
            return s[start]
        # characters are equal, advance inward
        if s[start] == s[end]:
            return s[start] + self.__longestPalindrome(s, start + 1, end - 1) + s[end]
        # characters arent equal, try both directions
        first = self.__longestPalindrome(s, start + 1, end)
        second = self.__longestPalindrome(s, start, end - 1)
        # return longest from either direction
        return first if len(first) >= len(second) else second
