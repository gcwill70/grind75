# sliding window


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(0, len(s)):
            # expand right
            right = i
            while right < len(s) and s[right] == s[i]:
                right += 1
            right -= 1
            # expand left and right
            left = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            # store if longest
            if right - left >= len(longest):
                longest = s[left : right + 1]
        return longest
