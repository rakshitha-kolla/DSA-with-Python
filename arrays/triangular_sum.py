from typing import List
'''
this gives O(n^2) time complexity and O(n) space complexity
we have to optimize it to O(n) time complexity and O(1) space complexity


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n-1):
            row=len(nums)
            for j in range(row-1):
                nums[j]=(nums[j]+nums[j+1])%10
        return nums[0]

'''

'''
Time Complexity
Worst Case: O(n)
You compute n binomial coefficients (using Pascal’s triangle or iterative formula), each in O(1) time if you use the iterative method.
Best Case: O(n)
No early exit; you always compute all coefficients.
Space Complexity
Worst Case: O(1)
Only a few variables are needed for the calculation.
Best Case: O(1)
'''

from math import comb
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(n):
            res += nums[i]*comb(n-1,i)
        return res%10    
s=Solution()    
print(s.triangularSum([1,2,3,4,5]))