class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        out = 0
        for num in nums:
            out = out ^ num
        return out
if __name__=="__main__":
    s=Solution()
    print(s.singleNumber([1]))