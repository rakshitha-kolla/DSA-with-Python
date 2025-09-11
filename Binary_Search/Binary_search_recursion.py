from typing import List
class Solution:
    def search(self, nums: List[int], target: int,high:int,low:int) -> int:
        if low>high:
            return -1
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return self.search(nums,target,mid-1,low)
        else:
            return self.search(nums,target,high,mid+1)
        
        
s=Solution()
print(s.search([-1,0,3,5,9,12],9,5,0))