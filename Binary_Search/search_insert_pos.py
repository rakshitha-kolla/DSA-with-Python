import bisect   
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1
        ans=high+1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos=bisect.bisect_left(nums,target)
        return pos
s=Solution()
print(s.searchInsert([1,3,5,6],5))  