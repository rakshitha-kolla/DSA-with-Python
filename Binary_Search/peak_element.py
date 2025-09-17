from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[high]>nums[high-1]:
            return high
        while(low<=high):
            mid=(low+high)//2
            if ((nums[mid]>nums[mid+1]) and (nums[mid]>nums[mid-1])):
                return mid
            if nums[mid]<nums[mid+1]:
                low=mid+1
            else:
                high=mid-1
        return -1
s=Solution()    
print(s.findPeakElement([1,2,3,1])) 