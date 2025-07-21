class Solution:
    def makeFancyString(self, s: str) -> str:
        c=1
        temp=s[0]
        prev=s[0]
        for i in range(1,len(s)):
            if s[i]==prev:
                c+=1
            else:
                prev=s[i]
                c=1
            if c<3:
                temp+=s[i]
        return temp
s=Solution()
print(s.makeFancyString("aaabaaaa"))