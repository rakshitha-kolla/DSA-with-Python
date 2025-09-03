from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev=intervals[0]
        new_array=[]
        for s,e in intervals[1:]:
            cur=[s,e]
            if prev[1]>=cur[0]:
                cur=[min(prev[0],cur[0]),max(cur[1],prev[1])]
            else:
                new_array.append(prev)
            prev=cur
        new_array.append(prev)
        return new_array
s=Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))