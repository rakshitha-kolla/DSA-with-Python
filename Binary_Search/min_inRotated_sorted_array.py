from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        ans=float('inf')
        while(low<=high):
            mid=(low+high)//2
            if nums[low]<=nums[high]:
                ans=min(ans,nums[low])
                break
            elif nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ans=min(ans,nums[mid])
                high=mid-1
        return ans

s=Solution()
print(s.findMin([3,4,5,1,2]))