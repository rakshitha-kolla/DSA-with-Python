import bisect
from typing import List
'''
class Solution:
    def upper(self,nums):
        low=0
        high=len(nums)-1
        ans=high+1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]>0:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans 
    def lower(self,nums):
        low=0
        high=len(nums)-1
        ans=high+1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]>=0:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans    
    def maximumCount(self, nums: List[int]) -> int:
        upper=self.upper(nums)
        lower=self.lower(nums)
        return max(len(nums)-upper,lower)'''
import bisect
class Solution:  
    def maximumCount(self, nums: List[int]) -> int:
        upper=bisect.bisect_left(nums,0)
        lower=bisect.bisect_right(nums,0)
        return max(lower,len(nums)-upper)
s=Solution()
print(s.maximumCount([-2,-1,-1,1,2,3])) 