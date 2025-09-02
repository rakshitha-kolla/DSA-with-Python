from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum=float('inf')
        min_diff=float('inf')
        n=len(nums)
        for i in range(n-2):
            left,right=i+1,n-1
            while(left<right):
                curr_sum=nums[i]+nums[left]+nums[right]
                curr_diff=abs(curr_sum-target)
                if curr_diff<min_diff:
                    min_diff=curr_diff
                    closest_sum=curr_sum
                if curr_sum<target:
                    left+=1
                elif curr_sum>target:
                    right-=1
                else:
                    return target
        return closest_sum
s=Solution()
print(s.threeSumClosest([-1,2,1,-4],1))