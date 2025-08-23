'''from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        max_count=0
        count=1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                count+=1
            else:
                count=1
            max_count=max(max_count,count)
        return max_count'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        if len(s) < 1:
            return 0
        elif len(s) ==1:
            return 1
        longest=1
        for num in s:
            if  num-1 not in s:
                count=1
                while num+count in s:
                    count+=1
                longest=max(longest,count)
        return longest
                 



s=Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))