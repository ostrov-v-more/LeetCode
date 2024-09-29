"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

nums = [1,3,5,6], target = 5 // 2
nums = [1,3,5,6], target = 2 // 1
nums = [1,3,5,6], target = 7 // 4
"""
import math

nums = [1,3,5,6]


class Solution(object):
    @staticmethod
    def search_insert(nums: list[int], target: int) -> int:
        """O(n)"""
        if target in nums:
            return nums.index(target)
        else:
            for i in nums:
                if i + 1 == target:
                    return nums.index(i) + 1

    @staticmethod
    def search_insert_2(self, nums: list[int], target: int) -> int:
        """O(log n)"""
        low = 0
        high = len(nums)

        while low < high:
            middle = (high + low) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] < target:
                low = middle + 1

            if nums[middle] > target:
                high = middle - 0
        return low

a = Solution.search_insert_2(nums=nums, target=5)
print(a)
