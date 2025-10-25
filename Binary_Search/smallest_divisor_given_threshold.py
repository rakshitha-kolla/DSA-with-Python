import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if threshold == len(nums):
            return max(nums)
        small=1
        large=max(nums)
        while(small<=large):
            mid=(small+large)//2
            s=0
            for num in nums:
                s+=math.ceil(num/mid)
            if s <= threshold:
                large=mid-1
            elif s > threshold:
                small=mid+1
        return small
