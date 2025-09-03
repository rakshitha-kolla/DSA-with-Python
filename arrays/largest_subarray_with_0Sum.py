class Solution:
    def maxLength(self, arr):
        # code here
        d=dict()
        max_len=0
        sub_sum=0
        count=0
        for i in range(len(arr)):
            sub_sum+=arr[i]
            if sub_sum == 0:
                max_len=max(count+1,max_len)
            if sub_sum in d:
                max_len=max(max_len,i-d[sub_sum])
            else:
                d[sub_sum]=i
            count+=1
        return max_len
s=Solution()
print(s.maxLength([15, -2, 2, -8, 1, 7, 10, 23]))
    