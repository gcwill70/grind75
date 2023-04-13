class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = {}
        for i in range(len(s)):
            letters.setdefault(s[i], 0)
            letters.setdefault(t[i], 0)
            letters[s[i]] += 1
            letters[t[i]] -= 1
        for val in letters.values():
            if val != 0:
                return False
        return True
