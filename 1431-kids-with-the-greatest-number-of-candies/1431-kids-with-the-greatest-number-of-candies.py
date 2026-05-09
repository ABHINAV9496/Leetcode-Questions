class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        result = []
        for candi in candies:
            result.append(candi + extraCandies >= maximum)

        return result
        
        