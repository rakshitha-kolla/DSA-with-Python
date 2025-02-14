#User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr):
        # Your code goes here
        stack=[]
        maxi=float('-inf')
        for num in arr:
            while stack and stack[-1]>=num:
                small=stack.pop()
                secsmall=num
                score=small+secsmall
                maxi=max(maxi,score)
            if stack:
                small=stack.pop()
                secsmall=num
                score=small+secsmall
                maxi=max(maxi,score)
            stack.append(num)
        return maxi
s=Solution()
print(s.pairWithMaxSum([782, 786, 381 ,367 ,923 ,547 ,520 ,294, 675, 154 ,511 ,359 ,100, 3 ,820]))