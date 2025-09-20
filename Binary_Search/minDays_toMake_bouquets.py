from typing import List
class Solution:
    def fun(self,mid,bloomDay,m,k):
        count=0
        ans=0
        for i in range(len(bloomDay)):
            if bloomDay[i]<=mid:
                count+=1
            else:
                ans+=(count)//k
                count=0
        ans+=(count)//k
        return ans
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        ans=-1
        if len(bloomDay)<m*k:
            return ans
        low=min(bloomDay)
        high=max(bloomDay)
        while(low<=high):
            mid=(low+high)//2
            num=self.fun(mid,bloomDay,m,k)
            if num>=m:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
s=Solution()
print(s.minDays([1,10,3,10,2],3,1))