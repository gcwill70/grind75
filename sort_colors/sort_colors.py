# single pass to count occurrences
# another pass to sort into correct section of array


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # count occurrences
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        # setup three pointers
        first = 0
        second = counts[0]
        third = second + counts[1]
        # sort zeros
        i = 0
        while i < counts[0]:
            if nums[i] == 0:
                i += 1
            elif nums[i] == 1:
                self.__swap(nums, i, second)
                second += 1
            else:
                self.__swap(nums, i, third)
                third += 1
        # sort ones
        i = counts[0]
        while i < counts[0] + counts[1]:
            if nums[i] == 0:
                self.__swap(nums, i, first)
                first += 1
            elif nums[i] == 1:
                i += 1
            else:
                self.__swap(nums, i, third)
                third += 1
        # sort twos
        i = counts[0] + counts[1]
        while i < len(nums):
            if nums[i] == 0:
                self.__swap(nums, i, first)
                first += 1
            elif nums[i] == 1:
                self.__swap(nums, i, second)
                second += 1
            else:
                i += 1
        return nums

    def __swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
