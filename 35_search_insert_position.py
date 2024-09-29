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
        if target in nums:
            return nums.index(target)
        else:
            for i in nums:
                if i + 1 == target:
                    return nums.index(i) + 1




a = Solution.search_insert(nums=nums, target=5)
print(a)
