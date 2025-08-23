from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        first_col=False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0]=0
                    if j != 0:
                        matrix[0][j]=0
                    else:
                        first_col=True
        for i in range(m-1,-1,-1):
            for j in range(n-1,0,-1):
                if matrix[i][j] == 0:
                    continue
                if matrix[i][0] == 0:
                    matrix[i][j]=0
                elif matrix[0][j]==0:
                    matrix[i][j]=0
        if first_col:
            for i in range(m):
                matrix[i][0]=0
s=Solution()
print(s.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))


        