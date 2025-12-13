from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counts=Counter(s)
        ans=[]
        for char,freq in counts.most_common():
            ans.append(char*freq)
        return ''.join(ans)
    
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        heap=[]
        for ch,count in freq.items():
            heapq.heappush(heap,(-count,ch))
        results=[]
        while heap:
            count,ch=heapq.heappop(heap)
            results.append(ch*(-count))
        return ''.join(results)
s=Solution()
print(s.frequencySort("tree"))  # Output: "eetr" or "eert