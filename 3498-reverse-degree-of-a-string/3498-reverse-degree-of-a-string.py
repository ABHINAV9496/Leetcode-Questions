class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        for i, ch in enumerate(s):
            total += (ord('z') - ord(ch) + 1) * (i + 1)

        return total    