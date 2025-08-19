class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        cnt, streak = 0, 0
        for num in nums:
            if num == 0:
                streak += 1
                cnt += streak
            else:
                streak = 0
        return cnt
s=Solution()    
print(s.zeroFilledSubarray([1,3,0,0,2,0,0,4]))  # Example usage