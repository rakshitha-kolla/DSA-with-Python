'''class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dict={}
        n=len(nums)
        for num in nums:
                if num in dict:
                    dict[num]+=1
                else:
                    dict[num]=1
        for c in dict:
            if dict[c] > n//2:
                return c'''
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count=0
        ele=0
        for num in nums:
            if count==0:
                count=1
                ele=num
            elif ele==num:
                count+=1
            else:
                count-=1
        return ele
if __name__=="__main__":
    s=Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))