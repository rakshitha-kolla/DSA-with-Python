from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low,high=0,len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[low]==nums[high]:
                low+=1
                high-=1
            elif nums[mid]<=nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
        return False
s=Solution()
print(s.search([2,5,6,0,0,1,2],0))