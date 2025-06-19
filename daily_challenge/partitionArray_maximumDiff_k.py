class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 1
        rec = nums[0]
        for num in nums:
            if num - rec > k:
                ans += 1
                rec = num
        return ans
s=Solution()
print(s.partitionArray( [3,6,1,2,5],  2))