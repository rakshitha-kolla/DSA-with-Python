class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum=0
        msum=-999999999999999999999999
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            sum+=nums[i]
            if sum>msum:
                msum=sum
            if sum<0:
                sum=0
        return msum
if __name__=="__main__":
    s=Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))