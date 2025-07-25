from collections import defaultdict
class Solution:
    def maxSum(self, nums: list[int]) -> int:
        sub_array=0
        flag=False
        d=defaultdict(int)
        for i in range(len(nums)):
            if not d[nums[i]] and nums[i]>=0:
                sub_array+=nums[i]
                flag=True
            d[nums[i]]+=1
        if not flag:
            m=-1234567
            for num in nums:
                if num>m:
                    m=num
            sub_array=m
        return sub_array
s=Solution()
print(s.maxSum([1,1,0,2,2]))