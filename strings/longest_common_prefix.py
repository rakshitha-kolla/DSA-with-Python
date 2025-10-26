class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        strs.sort()
        first=strs[0]
        last=strs[-1]
        n=min(len(first),len(last))
        ans=[]
        for i in range(n):
            if first[i] != last[i]:
                break
            ans.append(first[i])
        return ''.join(ans)
s=Solution()    
print(s.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"