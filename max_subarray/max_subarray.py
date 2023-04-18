# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         return self.__maxSubArray(nums, 0, None)

#     def __maxSubArray(self, nums, i, sum) -> int:
#         print(f"__maxSubArray({nums}, {i}, {sum})")
#         if i == len(nums):
#             return sum
#         # get max sum if first in sequence
#         maximum = self.__maxSubArray(nums, i + 1, nums[i])
#         # get max sum if middle of sequence
#         maximum = max(maximum, self.__maxSubArray(nums, i + 1, (sum or 0) + nums[i]))
#         # get max sum if excluded
#         maximum = max(maximum, self.__maxSubArray(nums, i + 1, None))
#         return maximum


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
