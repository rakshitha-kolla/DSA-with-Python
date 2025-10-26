class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        elif s==t:
            return True
        freq={}
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        for i in range(len(t)):
            if t[i] not in freq or freq[t[i]]==0:
                return False
            else:
                freq[t[i]]-=1
        return True
        
s=Solution()
print(s.isAnagram("anagram","nagaram"))  # True
