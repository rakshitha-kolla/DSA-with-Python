from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        if n == 1:
            return [nums]
        def backtracking(path,used,res):
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i]=True
                backtracking(path,used,res)
                path.pop()
                used[i]=False
        res=[]
        backtracking([],[False]*n,res)
        return res
s=Solution()
print(s.permute([1,2,3]))  # Output should be [[1,