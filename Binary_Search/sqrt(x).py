from typing import List
class Solution:
    def mySqrt(self, x: int) -> int:
        low,high=1,x//2
        ans=1
        if x==0:
            return 0
        while(low<=high):
            mid=(low+high)//2
            if mid*mid<=x:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
s=Solution()
print(s.mySqrt(8))