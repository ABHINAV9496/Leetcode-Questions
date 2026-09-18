class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        once=max(len(seg)for seg in s.split('0'))    
        zeroes=max(len(seg)for seg in s.split('1'))
        return once>zeroes