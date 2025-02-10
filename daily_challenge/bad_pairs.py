class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        good_pairs=0
        n=len(nums)
        total_pairs= (n*(n-1))//2
        freq={}
        for i in range(n):
           key=nums[i]-i
           good_pairs+=freq.get(key,0)
           freq[key]=freq.get(key,0)+1
        return total_pairs-good_pairs
if __name__=="__main__":
    s=Solution()
    print(s.countBadPairs([4,1,3,3]))