class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = 0  # number of pairs meeting the requirements
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (i * j) % k == 0 and nums[i] == nums[j]:
                    res += 1
        return res
s=Solution()
print(s.countPairs([3,1,2,2,2,1,3],2))