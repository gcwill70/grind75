from collections import deque
from math import ceil, floor


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == None:
            return False
        s = "".join([i.lower() for i in s if i.isalpha()])
        if len(s) == 0:
            return False
        if len(s) % 2 != 0:
            split = floor(len(s) / 2)
            s = s[0:split] + s[split + 1 :]
        queue = deque()
        queue.append(s[0])
        for i in range(1, len(s)):
            if i < len(s) / 2:
                queue.append(s[i])
            elif s[i] == queue[-1]:
                queue.pop()
        return len(queue) == 0
