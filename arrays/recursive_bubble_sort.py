class Solution:
    def bubbleSort(self, nums,n=None):
        if n is None:
            n=len(nums)
        if n<=1:
            return nums
        swapped=False
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
                swapped=True
        if swapped:
            return self.bubbleSort(nums,n-1)
        return nums
s=Solution()
arr=[2, 1, 6, 10, 4, 1, 3, 9, 7]
print(s.bubbleSort(arr))
