from typing import List 
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while(low<=high):
            mid=(low+high)//2
            s=0
            d=1
            for num in weights:
                if s+num > mid:
                    s=num
                    d+=1
                else:
                    s+=num
            if d <= days:
                high=mid-1
            else:
                low=mid+1
        return low
s=Solution()
print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))