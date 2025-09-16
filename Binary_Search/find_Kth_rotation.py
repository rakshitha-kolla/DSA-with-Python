class Solution:
    def findKRotation(self, arr):
        # code here
        low,high=0,len(arr)-1
        idx=-1
        ans=float('inf')
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]<=arr[high]:
                if arr[mid]<=ans:
                    ans=arr[mid]
                    idx=mid
                high=mid-1
            else:
                if arr[low]<=ans:
                    idx=low
                    ans=arr[low]
                low=mid+1
        return idx
s=Solution()
print(s.findKRotation([5, 1, 2, 3, 4]))