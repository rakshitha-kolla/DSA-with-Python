class Solution:
    def leaders(self, arr):
        n=len(arr)
        leader=[]
        if n < 1:
            return leader
        elif n == 1:
            leader.append(arr[-1])
            return leader
        elif n == 2:
            if arr[-2]>=arr[-1]:
                leader.extend(arr)
                return leader
            else:
                leader.append(arr[-1])
                return leader
        
        leader.append(arr[-1])
        maxi=arr[-1]
        for i in range(n-2,-1,-1):
            if arr[i] >= maxi:
                leader.append(arr[i])
                maxi=arr[i]
        return self.reverse(leader)
    def reverse(self,leader):
        i,j=0,len(leader)-1
        while(i<j):
            leader[i],leader[j]=leader[j],leader[i]
            i+=1
            j-=1
        return leader
s=Solution()
print(s.leaders([16,17,4,3,5,2]))