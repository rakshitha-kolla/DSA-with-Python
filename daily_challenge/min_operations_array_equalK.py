class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        st = set()
        for x in nums:
            if x < k:
                return -1
            elif x > k:
                st.add(x)
        return len(st)
s=Solution()
print(s.minOperations([2,1,2],2))