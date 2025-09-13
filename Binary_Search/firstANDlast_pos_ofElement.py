from typing import List
class Solution:
    def lower_bound(self,nums,target):
        low,high=0,len(nums)-1
        start=high+1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]>=target:
                start=mid
                high=mid-1
            else:
                low=mid+1
        return start
    def upper_bound(self,nums,target):
        low,high=0,len(nums)-1
        last=high+1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]>target:
                last=mid
                high=mid-1
            else:
                low=mid+1
        return last
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=self.lower_bound(nums,target)
        last=self.upper_bound(nums,target)
        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        return [start,last-1]
s=Solution()        
print(s.searchRange([5,7,7,8,8,10],8)) 