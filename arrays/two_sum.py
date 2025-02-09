class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in hash:
                return [hash[complement],i]
            hash[nums[i]]=i
if __name__=="__main__":
    s=Solution()
    print(s.twoSum([2,7,11,15],9))