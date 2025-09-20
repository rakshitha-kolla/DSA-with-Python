from typing import List
import math
class Solution:
    def numhours(self,mid,piles,h):
        count=0
        for num in piles:
            count+=math.ceil(num/mid)
            if count>h:
                return False
        return True
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans=float('inf')
        low,high=1,max(piles)
        while(low<=high):
            mid=(low+high)//2
            if self.numhours(mid,piles,h):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
s=Solution()
print(s.minEatingSpeed([3,6,7,11],8))
