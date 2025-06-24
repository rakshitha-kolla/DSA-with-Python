class Solution:
    def findKDistantIndices(
        self, nums: list[int], key: int, k: int
    ) -> list[int]:
        res = []
        n = len(nums)
        # traverse number pairs
        for i in range(n):
            for j in range(n):
                if nums[j] == key and abs(i - j) <= k:
                    res.append(i)
                    break  # early termination to prevent duplicate addition
        return res
s=Solution()
print(s.findKDistantIndices( [3,4,9,1,3,9,5],  9,  1))