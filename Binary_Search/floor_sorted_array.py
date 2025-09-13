
class Solution:
    def findFloor(self, arr, x):
        # code here
        high=len(arr)-1
        low=0
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]<=x:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
s=Solution()
print(s.findFloor([1,2,8,10,10,12,19],9))
#User function Template for python3