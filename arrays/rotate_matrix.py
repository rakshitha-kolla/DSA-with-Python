from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        #transpose firt
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            s,e = 0,n-1
            while(s<e):
                matrix[i][e],matrix[i][s]=matrix[i][s],matrix[i][e]
                s+=1
                e-=1
        

s= Solution()
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
s.rotate(matrix)
print(matrix)