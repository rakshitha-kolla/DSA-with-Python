from collections import defaultdict
class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        dict=defaultdict(list)
        for num in nums:
            t=num
            s=0
            while(t):
                r=t%10
                s+=r
                t=t//10
            dict[s].append(num)
        sum=-1
        for l in dict.values():
            if len(l)<=1:
                continue
            elif len(l)==2:
                num1=l[0]
                num2=l[1]
                sum=max(sum,num1+num2)
            else:
                large=0
                sl=0
                for num in l:
                    if num >large:
                        sl=large
                        large=num
                    if num>sl and num<large:
                        sl=num
                sum=max(sum,large+sl)
        return sum
if __name__=="__main__":
    s=Solution()
    print(s.maximumSum([10,12,19,14]))