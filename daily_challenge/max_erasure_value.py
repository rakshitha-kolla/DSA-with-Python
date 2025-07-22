class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        subarray=0
        s=0
        seen=set()
        l=0
        for r in range(len(nums)):
            while(nums[r] in seen):
                seen.remove(nums[l])
                s-=nums[l]
                l+=1
            s+=nums[r]
            seen.add(nums[r])
            subarray=max(s,subarray)
        return subarray
s=Solution()
print(s.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))