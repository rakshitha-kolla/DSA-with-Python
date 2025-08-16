class Solution:
    def maximum69Number (self, num: int) -> int:
        l=[]
        temp=num
        while temp:
            l.append(temp%10)
            temp = temp //10
        l.reverse()
        maxi=num
        for i in range(len(l)):
            if l[i] == 9:
                continue
            l[i]=9
            break
        l=[str(n) for n in l]
        s=''.join(l)
        return int(s)
s=Solution()
print(s.maximum69Number(9669))  # Output: 9969
print(s.maximum69Number(9996))  # Output: 9999
print(s.maximum69Number(9999))  # Output: 9999