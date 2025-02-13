import heapq
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        op=0
        heapq.heapify(nums)
        while(nums):
            s=heapq.heappop(nums)
            if s>=k:
                return op
            if not nums:
                retrurn -1
            s2=heapq.heappop(nums)
            heapq.heappush(nums,s*2 + s2)
            op+=1
        return -1

if __name__=="__main__":
    s=Solution()
    o=s.minOperations( [2,11,10,1,3],10)
    print(o)