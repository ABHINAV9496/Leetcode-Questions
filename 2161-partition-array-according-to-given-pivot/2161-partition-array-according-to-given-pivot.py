class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        ans=[]
        for num in nums:
            if num<pivot:
                ans.append(num)
        for num in nums:
            if num == pivot:
                ans.append(num)
        for num in nums:
            if num>pivot:
                ans.append(num)
        return ans                        
        