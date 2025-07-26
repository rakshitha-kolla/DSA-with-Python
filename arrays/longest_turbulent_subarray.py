class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        max_length=1
        start=0
        p=0
        c=0
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                c=1
            elif arr[i-1]<arr[i]:
                c=-1
            else:
                c=0
            if  c == 0:
                start=i
            elif p==c:
                    start=i-1
            p=c
            max_length=max(max_length,i-start+1)
        return max_length
s=Solution()
print(s.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))