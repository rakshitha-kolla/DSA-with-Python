class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        result=0
        for num in nums:
            result |= num
        return result << (len(nums)-1)
s=Solution()
print(s.subsetXORSum([3,4,5,6,7,8]))