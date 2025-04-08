class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        seen = [False] * 128
        for i in range(len(nums) - 1, -1, -1):
            if seen[nums[i]]:
                return i // 3 + 1
            seen[nums[i]] = True
        return 0
s=Solution()
print(s.minimumOperations([1,2,3,4,2,3,3,5,7]))