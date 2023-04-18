# 1: AAAA BBBB -> do nothing
# 2: AAABABBB -> [A.start, B.end]
# 3: AABBBBAAA -> do nothing
# 4: BBAABBAAA -> [B.start, A.end]
# 5: BBAAAABB -> [B.start, B.end]
# 6: BBBB AAAA -> do nothing


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        # insert newInterval and sort
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        # merge intervals
        start = intervals[0][0]
        end = intervals[0][1]
        merged = []
        for interval in intervals:
            if interval[0] <= end:  # check for overlap
                end = max(end, interval[1])
            else:  # no overlap
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
        merged.append([start, end])
        return merged
