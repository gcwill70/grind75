# solution 1: left and right pointers. check counts of each character. if s[left] count too high, increment left. if s[right] count too high, increment right. O(N^2)

# solution 2: first loop for window length. second loop for moving window across. third loop for checking if all of t is in s. O(N^2)


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # check if t is in all of s
        tmp = s
        for elem in t:
            idx = s.find(elem)
            if idx != -1:
                tmp = tmp[0:idx] + tmp[idx + 1 : -1]
            else:
                return ""
        # make hash map of characters
        s_map = {}
        for elem in s:
            s_map.setdefault(elem, 0)
            s_map[elem] += 1
        t_map = {}
        for elem in t:
            t_map.setdefault(elem, 0)
            t_map[elem] += 1
        # initialize left and right pointers
        left = 0
        right = len(s) - 1
        changed = True
        # narrow down window
        while left <= right and changed:
            changed = False
            # increment left
            if s_map[s[left]] > t_map.get(s[left], 0):
                s_map[s[left]] -= 1
                left += 1
                changed = True
            # decrement right
            if s_map[s[right]] > t_map.get(s[right], 0):
                s_map[s[right]] -= 1
                right -= 1
                changed = True
        return s[left : right + 1]
