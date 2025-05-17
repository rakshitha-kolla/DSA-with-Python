class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        for i in range(3):
            l.append(nums.count(i))
        nums[::]=[]
        for i in range(len(l)):
            nums.extend([i for k in range(l[i])])
s=Solution()
print(s.sortColors([2,0,2,1,1,0]))