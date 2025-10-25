from typing import List 
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=''
        c=0
        for char in s:
            if char == '(':
                if c==0:
                    c+=1
                else:
                    c+=1
                    ans+=char
            else:
                c-=1
                if c!=0:
                    ans+=char
        return ans
s=Solution()
print(s.removeOuterParentheses("(()())(())"))  # Output: "()()()