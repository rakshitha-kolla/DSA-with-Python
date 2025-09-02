from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for row in range(numRows):
            res=1
            l=[]
            l.append(res)
            for col in range(1,row+1):
                res=res*(row-(col-1))   
                res=res//col
                l.append(res)
            ans.append(l)
        return ans
s=Solution()
print(s.generate(5))