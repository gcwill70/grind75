class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i] + [num])
        return subsets
