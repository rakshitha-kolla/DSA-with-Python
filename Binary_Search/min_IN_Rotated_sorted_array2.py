from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        ans=float('inf')
        while(low<=high):
            mid=(low+high)//2
            if nums[low]==nums[mid]==nums[high]:
                ans=min(ans,nums[mid])
                low+=1
                high-=1
            elif nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ans=min(ans,nums[mid])
                high=mid-1
        return ans
s=Solution()
print(s.findMin([2,2,2,0,1]))