from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        idx=-1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                idx=i
                break
        if idx >= 0:
            for i in range(n-1,idx,-1):
                if nums[i] > nums[idx]:
                    self.swap(nums,idx,i)
                    break
        self.reverse(nums,idx+1)
    def swap(self,nums,idx,i):
        temp=nums[idx]
        nums[idx]=nums[i]
        nums[i]=temp
    def reverse(self,nums,start):
        i,j=start,len(nums)-1
        while(i<j):
            self.swap(nums,i,j)
            i+=1
            j-=1
s=Solution()
nums=[1,2,3]
s.nextPermutation(nums)
print(nums)  # Output should be [1,3,2]
