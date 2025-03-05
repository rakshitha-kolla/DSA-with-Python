'''There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:

    At the first minute, color any arbitrary unit cell blue.
    Every minute thereafter, color blue every uncolored cell that touches a blue cell.
Return the number of colored cells at the end of n minutes.
Example 1:

Input: n = 1
Output: 1
Explanation: After 1 minute, there is only 1 blue cell, so we return 1.

Example 2:

Input: n = 2
Output: 5
Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5.
'''

'''
class Solution:
    def coloredCells(self, n: int) -> int:
        return 2*n*(n-1)+1
'''

class Solution:
    def coloredCells(self, n: int) -> int:
        num = 1
        diff = 4
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(2, n + 1):
                num += diff
                diff += 4

        return num
s=Solution()
print(s.coloredCells(3))