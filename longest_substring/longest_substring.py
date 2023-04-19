class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        start = 0
        end = 0
        maxCount = 0
        table = set()
        while end < len(s):
            if s[end] not in table:
                table.add(s[end])
                end += 1
            else:
                start += 1
                end = start
                table.clear()
            maxCount = max(maxCount, len(table))
        return maxCount
