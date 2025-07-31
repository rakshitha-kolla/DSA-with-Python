class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        max_or_value = 0
        for num in nums:
            max_or_value |= num
        total_subsets = 1 << len(nums)
        subsets_with_max_or=0
        for i in range(total_subsets):
            current_or_value=0
            for j in range(len(nums)):
                if i & (1<<j):
                    current_or_value|=nums[j]
            if current_or_value == max_or_value:
                subsets_with_max_or+=1
        return subsets_with_max_or
s=Solution()
print(s.countMaxOrSubsets([1,2,3]))