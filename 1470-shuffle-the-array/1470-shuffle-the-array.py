class Solution(object):
    def shuffle(self, nums, n):
        for i in range(n):
            yield nums[i]
            yield nums[i + n]