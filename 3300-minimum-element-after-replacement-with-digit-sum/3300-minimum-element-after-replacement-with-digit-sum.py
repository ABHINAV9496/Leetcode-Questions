class Solution:
    def minElement(self, nums):
        minimum = float('inf')

        for num in nums:
            digit_sum = 0

            for digit in str(num):
                digit_sum += int(digit)

            if digit_sum < minimum:
                minimum = digit_sum

        return minimum