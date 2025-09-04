from typing import List
class Solution:
    def findErrorNums(self, nums):
        n=len(nums)
        s1,s2=0,0
        sn1=n*(n+1)//2
        sn2=n*(n+1)*(2*n+1)//6
        for num in nums:
            s1+=num
            s2+=(num*num)
        val1=s1-sn1 #x-y
        val2=s2-sn2 
        val2=(val2)//val1#x+y
        duplicate=(val1+val2)//2
        return [duplicate,duplicate-val1]
s=Solution()
print(s.findErrorNums([1,2,2,4]))