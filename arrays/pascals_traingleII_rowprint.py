from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=1
        row=[1]
        for col in range(1,rowIndex+1):
            res=res*(rowIndex-(col-1))
            res=res//col
            row.append(res)
        return row
s=Solution()
print(s.getRow(3))