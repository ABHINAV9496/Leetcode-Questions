class Solution(object):
    def subtractProductAndSum(self, n):
        prod=1 
        sum=0
        s=str(n)

        for c in s:
            digit=int(c)
            prod *= digit
            sum += digit

        return prod-sum    

        
        