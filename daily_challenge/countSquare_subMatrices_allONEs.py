from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r=0
        dp=list()
        for i in matrix:
            dp.append([])
            r+=1
        c=len(matrix[0])
        for i in range(r):
            for j in range(c):
                dp[i].append(0)
        for i in range(r):
            dp[i][0]=matrix[i][0]
        for i in range(c):
            dp[0][i]=matrix[0][i]
        if r==0 or c==0:
            return 0
        if r==1 and c==1:
            return matrix[0][0]
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] =1 + min(dp[i-1][j],min(dp[i][j-1],dp[i-1][j-1]))
        sumi=0
        for i in range(r):
            for j in range(c):
                sumi+=dp[i][j]
        return sumi
s=Solution()
print(s.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))  # Output: 15
print(s.countSquares([[1,0,1],[1,1,0],[1,1,0]]))  # Output: 7
print(s.countSquares([[0]]))  # Output: 0
print(s.countSquares([[1]]))  # Output: 1
print(s.countSquares([[0,0],[0,0]]))  # Output: 0