class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        dict={}
        l=[]
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        for num in dict:
            if dict[num] != 2:
                l.append(num)
        return l
if __name__=="__main__":
    s=Solution()
    print(s.singleNumber([0,0,1]))
