'''Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
Example 1:
Input: nums = [2,2,3,2]
Output: 3
Example 2:S
Input: nums = [0,1,0,1,0,1,99]
Output: 99
'''

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones,twos=0,0
        for num in nums:
            ones = ones ^ num & ~ twos
            twos = twos ^ num & ~ones
        return ones
if __name__=="__main__":
    s=Solution()
    print(s.singleNumber([0,1,0,1,0,1,99]))

'''Example Walkthrough process :
Input: nums = [2,2,3,2]

    Start with ones = 0, twos = 0.
    Process 2:
        ones = (0 ^ 2) & ~0 = 2
        twos = (0 ^ 2) & ~2 = 0
    Process 2 again:
        ones = (2 ^ 2) & ~0 = 0
        twos = (0 ^ 2) & ~0 = 2
    Process 2 again:
        ones = (0 ^ 2) & ~2 = 0
        twos = (2 ^ 2) & ~0 = 0
    Process 3:
        ones = (0 ^ 3) & ~0 = 3
        twos = (0 ^ 3) & ~3 = 0
    Result: ones = 3
'''