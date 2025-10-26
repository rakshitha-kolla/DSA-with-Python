class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table={}
        for i in range(len(s)):
            if s[i]!=t[i]:
                if s[i] not in table:
                    if t[i] not in table.values():              
                        table[s[i]]=t[i]
                    else:
                        return False
                else:
                    if table[s[i]] != t[i]:
                        return False
            else:
                if s[i] in table:
                    if table[s[i]]!=t[i]:
                        return False
                elif t[i] in table.values():
                    return False
                table[s[i]]=t[i]

        return True
S=Solution()
print(S.isIsomorphic("egg","add"))