class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        ans=''
        for i in range(len(l)-1,-1,-1):
            ans+=l[i]
            ans+=" "
        return ans.strip()
s=Solution()
print(s.reverseWords("  hello world  "))  # Output: "world hello"