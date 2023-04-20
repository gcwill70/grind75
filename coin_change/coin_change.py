from collections import deque


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        q = deque([amount])
        visited = set()
        depth = 0
        while q:
            # for each node at this level
            for i in range(len(q)):
                amt = q.popleft()
                if amt < 0:
                    continue
                elif amt == 0:
                    return depth
                # add neighbors
                elif amt not in visited:
                    visited.add(amt)
                    for c in coins:
                        q.append(amt - c)
            depth += 1
        return -1
