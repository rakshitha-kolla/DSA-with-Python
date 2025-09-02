from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        c1,c2=None,None
        count1,count2=0,0
        for num in nums:
            if c1==num:
                count1+=1
            elif c2 == num:
                count2+=1
            elif count1==0:
                c1,count1=num,1
            elif count2==0:
                c2,count2=num,1
            else:
                count1-=1
                count2-=1
        res=[]
        for c in [c1,c2]:
            if c is not None and nums.count(c)>n//3:
                res.append(c)
        return res

s=Solution()
print(s.majorityElement([3,2,3]))