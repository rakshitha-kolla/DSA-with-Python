
class Solution:
    def power(self,mid,n,m):
        ans=1
        for i in range(n):
            ans=ans*mid
            if ans>m:
                return 0
        if ans == m:
            return 1
        else:
            return 2
    def nthRoot(self, n, m):
       # code here
       low=1
       high=m
       while(low<=high):
            mid=(low+high)//2
            got=self.power(mid,n,m)
            if got==0:
                high=mid-1
            elif got == 1:
                return mid
            else:
                low=mid+1
       return -1
s=Solution()
print(s.nthRoot(3,27))