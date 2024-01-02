'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

nums = [3, 2, 2, 3]
val = 3


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums[:] = list(filter((val).__ne__, nums))  # 16.34 mb
        # nums[:] = list(filter(lambda a: a != val, nums)) # 16.39 mb
        # nums[:] = [i for i in nums if i != val]  # 16,32 mb
        return len(nums)


