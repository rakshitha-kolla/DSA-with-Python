class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > 0:
            k = k % len(nums)
            nums[:] = nums[-k:] + nums[:-k]
        print(nums)
s=Solution()
s.rotate([1,2,3,4,5,6,7],3)
