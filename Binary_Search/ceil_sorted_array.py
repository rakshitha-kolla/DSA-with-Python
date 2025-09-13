#User function Template for python3
class Solution:
    def findCeil(self, arr, x):
        # code here
        low=0
        high=len(arr)-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]<x:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans
s=Solution()
print(s.findCeil([1,2,8,10,10,12,19],5))