import bisect
from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans=0
        for i in range(len(grid)):
            low=0
            n=len(grid[i])
            high=n-1
            c=n
            while(low<=high):
                mid=(low+high)//2
                if grid[i][mid]<0:
                    c=mid
                    high=mid-1
                else:
                    low=mid+1
            ans+=(n-c)
        return ans

s=Solution()
print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))