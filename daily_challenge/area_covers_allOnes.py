from typing import List
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        low_x=10**3
        high_x=-1
        low_y=10**3
        high_y=-1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    low_x = min(low_x,i)
                    high_x=max(high_x,i)
                    low_y=min(low_y,j)
                    high_y=max(high_y,j)
        return (high_x-low_x+1)*(high_y-low_y+1)
s=Solution()
print(s.minimumArea([[1,0,0,0],[0,1,1,0],[0,1,0,0],[0,0,0,0]]))