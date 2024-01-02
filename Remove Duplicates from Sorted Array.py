'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.
'''


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int: # 95 ms / 17.72 mb
        nums2 = list(sorted(set(nums)))
        for i in range(len(nums)):
            if i < len(nums2):
                nums[i] = nums2[i]
                i += 1
            else:
                nums.pop()
        return len(nums)

    def removeDuplicates2(self, nums: list[int]) -> int:  # 84 ms / 17,66 mb
        nums[:] = list(sorted(set(nums)))
        return len(set(nums))




nums = [-1,0,0,1,1,2,2,3,3,4] # nums2 = [-1, 0, 1, 2, 3, 4]
print(Solution().removeDuplicates(nums))
