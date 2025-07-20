class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
        freq={}
        for ele in nums:
            freq[ele]=freq.get(ele,0)+1
        return [[key,ele] for key,ele in freq.items()]
if __name__=="__main__":
    nums= [5, 5, 5, 5]
    s=Solution()
    print(s.countFrequencies(nums))
"""

Input: nums = [1, 2, 2, 1, 3]

Output: [[1, 2], [2, 2], [3, 1]]

Explanation:

- 1 appears 2 times

- 2 appears 2 times

- 3 appears 1 time

Order of output can vary."""