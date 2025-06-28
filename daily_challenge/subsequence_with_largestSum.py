class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        vals = [[i, nums[i]] for i in range(n)]  # auxiliary array
        # sort by numerical value in descending order
        vals.sort(key=lambda x: -x[1])
        # select the first k elements and sort them in ascending order by index
        vals = sorted(vals[:k])
        res = [val for idx, val in vals]  # target subsequence
        return res
s=Solution()
print(s.maxSubsequence( [2,1,3,3], 2))