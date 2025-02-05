'''Given an array of positive integers nums,
return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
'''
class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        sub={}
        sum=nums[0]
        sub[sum]=0
        n=len(nums)
        if n<=1:
            return nums[0]
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                sum+=nums[i]
            else:
                sum=nums[i]
            sub[sum]=i
        max=-10000
        for k in sub:
            if k>max:
                max=k
        return max
s=Solution()
print(s.maxAscendingSum([100,10,1]))