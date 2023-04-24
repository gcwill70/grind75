class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # sort intervals by first
        intervals.sort(key=lambda x: x[0])
        # create merged interval array
        merged = [[intervals[0][0], intervals[0][1]]]
        i = 0
        # insert each item, starting at earliest interval
        for j in range(1, len(intervals)):
            if merged[i][1] >= intervals[j][0]:
                merged[i] = [merged[i][0], max(merged[i][1], intervals[j][1])]
            else:
                merged.append([intervals[j][0], intervals[j][1]])
                i += 1
        return merged
