from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod=-float('inf')
        prefix=1
        suffix=1
        n=len(nums)
        for i in range(len(nums)):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix=prefix*nums[i]
            suffix=suffix*nums[n-i-1]
            maxprod=max(maxprod,max(prefix,suffix))
        return maxprod
s=Solution()    
print(s.maxProduct([2,3,-2,4]))