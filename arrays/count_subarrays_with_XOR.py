class Solution:
    def subarrayXor(self, arr, k):
        # code here
        count=0
        s=dict()
        xr=0
        for i in range(len(arr)):
            xr=arr[i]^xr
            if xr == k:
                count+=1
            if xr^k in s:
                count+=s[xr^k]
            s[xr]=s.get(xr,0)+1
        return count
                
s=Solution()
print(s.subarrayXor([4,2,2,6,4],6))
        # code here