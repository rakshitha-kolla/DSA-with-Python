from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(start,curr):
            result.append(curr[:])
            for i in range(start,len(nums)):
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()
        backtrack(0,[])
        return result
# using bit manupulaiton
class Sol:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=[]
        for i in range(1<<n):
            subset=[]
            for j in range(n):
                if i&(1<<j):
                    subset.append(nums[j])
            result.append(subset)
        return result
s=Solution()
print(s.subsets([1,2,3]))
s1=Sol()
print(s1.subsets([1,2,3]))