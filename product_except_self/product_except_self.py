#


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)
        pre = post = 1
        for i in range(len(nums)):
            answer[i] *= pre
            pre *= nums[i]
            answer[-1 - i] *= post
            post *= nums[-1 - i]
        return answer
