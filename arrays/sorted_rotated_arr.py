'''Given an array nums, return true if the array was originally sorted in non-decreasing order,
 then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
'''
class Solution:
    def check(self, nums: list[int]) -> bool:
        sor_arr=nums.copy()
        for i in range(1,len(sor_arr)):
            t=sor_arr[i]
            j=i-1
            while(j>=0 and sor_arr[j]>t):
                sor_arr[j+1]=sor_arr[j]
                j-=1
            sor_arr[j+1]=t
        c=0
        while(c<len(nums)):
            if nums[c:] + nums[:c] == sor_arr:
                return True
            c+=1
        return False
s=Solution()
ans=s.check([11,12,1,18,2,5,6])
print(ans)