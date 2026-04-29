class Solution(object):
    def sumOfMultiples(self, n):
        result=[]
        for num in range(1,n+1):
            if num%3==0 or num%5==0 or num%7==0:
                result.append(num)    
        return sum(result)        

 