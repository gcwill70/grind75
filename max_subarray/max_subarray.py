class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            curSum = 0 if curSum < 0 else curSum
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum
