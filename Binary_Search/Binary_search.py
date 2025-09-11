from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        high=n-1
        low=0
        while(low<=high):
            mid=(high+low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1
        
s=Solution()
print(s.search([-1,0,3,5,9,12],9))