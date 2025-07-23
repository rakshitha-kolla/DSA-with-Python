import heapq
from typing import List
'''class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap=[]
        for num in nums:
            heapq.heappush(min_heap,num)
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return min_heap[0]'''

class Solution():
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
s=Solution()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))