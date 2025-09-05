from typing import List
class Solution:
    def mergesort(self,nums,low,high):
        count=0
        if low<high:
            mid=(low+high)//2
            count+=self.mergesort(nums,low,mid)
            count+=self.mergesort(nums,mid+1,high)
            count+=self.merge(nums,low,mid,high)
        return count
    def merge(self,nums,low,mid,high):
        left=low
        right=mid+1
        count=0
        new=[]
        for i in range(left,mid+1):
            while(right<=high and nums[i]>2*nums[right]):
                right+=1
            count+=(right-(mid+1))
        right=mid+1
        while(left<=mid and right <= high):
            if nums[left] < nums[right]:
                new.append(nums[left])
                left+=1
            else:
                new.append(nums[right])
                right+=1
        while(left<=mid):
            new.append(nums[left])
            left+=1
        while(right<=high):
            new.append(nums[right])
            right+=1
        for i in range(len(new)):
            nums[low]=new[i]
            low+=1
        return count
    def reversePairs(self, nums: List[int]) -> int:
        n=len(nums)
        count=self.mergesort(nums,0,n-1)
        return count
s=Solution()
print(s.reversePairs([1,3,2,3,1]))