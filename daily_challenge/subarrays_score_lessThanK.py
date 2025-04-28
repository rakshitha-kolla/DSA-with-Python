class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res, total = 0, 0
        i = 0
        for j in range(n):
            total += nums[j]
            while i <= j and total * (j - i + 1) >= k:
                total -= nums[i]
                i += 1
            res += j - i + 1
        return res
s=Solution()
print(s.countSubarrays([2,1,4,3,5],10))