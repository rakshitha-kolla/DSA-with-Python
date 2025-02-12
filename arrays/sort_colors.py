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
if __name__=="__main__":
    s=Solution()
    nums=[2,0,2,1,1,0]
    s.sortColors(nums)
    print(nums)