class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        x = s[:k]
        y = x[::-1]
        return y + s[k:]
        