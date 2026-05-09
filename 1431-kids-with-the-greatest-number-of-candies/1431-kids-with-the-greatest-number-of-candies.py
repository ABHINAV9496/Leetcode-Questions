class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)

        result = []

        for c in candies:
            result.append(c + extraCandies >= maximum)

        return result
        
        