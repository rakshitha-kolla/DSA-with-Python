'''Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        c_max=0
        m=0
        for num in nums:
            if num == 1:
                m+=1
            else:
                if c_max < m:
                    c_max=m
                m=0
        if c_max<m:
            c_max=m
        return c_max
if __name__=="__main__":
    s=Solution()
    out=s.findMaxConsecutiveOnes([1,1,0,1,1,1])
    print(out)