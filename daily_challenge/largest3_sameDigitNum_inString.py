class Solution:
    def largestGoodInteger(self, num: str) -> str:
        substr=set()
        count=1
        for i in range(1,len(num)):
            if num[i] == num[i-1]:
                count+=1
            else:
                count=1
            if count == 3:
                substr.add(num[i-2:i+1])
        if len(substr) == 0:
            return ""
        elif len(substr) == 1:
            return next(iter(substr))
        else:
            m=-1
            for n in substr:
                number=int(n)
                if number > m:
                    m=number
        return str(m)

s=Solution()
print(s.largestGoodInteger("6777133339"))  # Output: "777"
print(s.largestGoodInteger("2300019"))     # Output: "000"
print(s.largestGoodInteger("42352338"))
