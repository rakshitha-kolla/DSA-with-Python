from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)//2
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
        for k in d.keys():
            if d[k] > majority:
                return k
s=Solution()
print(s.majorityElement([3,2,3]))