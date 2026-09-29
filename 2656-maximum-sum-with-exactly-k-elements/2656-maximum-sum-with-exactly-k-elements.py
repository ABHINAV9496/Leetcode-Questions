class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maximum = max(nums)
        answer = 0
        for i in range(k):
            answer += maximum
            maximum += 1
        return answer