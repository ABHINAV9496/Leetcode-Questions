class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c0 = nums.count(0)
        c1 = nums.count(1)
        c2 = nums.count(2)

        i = 0

        for _ in range(c0):
            nums[i] = 0
            i += 1

        for _ in range(c1):
            nums[i] = 1
            i += 1

        for _ in range(c2):
            nums[i] = 2
            i += 1   