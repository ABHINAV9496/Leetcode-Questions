class Solution(object):
    def digitFrequencyScore(self, n):
        count = {}

        for digit in str(n):
            count[digit] = count.get(digit, 0) + 1

        ans = 0

        for digit in count:
            ans += int(digit) * count[digit]

        return ans
