# solution 1: brute force.
# for each domino, rotate all other dominos and check if numbers are the same each time. O(2^N)

# solution 2:
# count frequencies of each side - O(N)
# for each side, get rotations needed then update min - O(N)


from collections import Counter


class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)
        # count frequencies
        same = Counter()
        cntt = Counter(tops)
        cntb = Counter(bottoms)
        # count same elements
        for a, b in zip(tops, bottoms):
            if a == b:
                same[a] += 1
        # try each side
        for i in range(1, 7):
            if cntt[i] + cntb[i] - same[i] == n:
                # get rotations required
                return min(cntt[i], cntb[i]) - same[i]
        return -1
