'''Longest Subarray with Sum K
Given an array arr[] containing integers and an integer k,
your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.
Examples:

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.

Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Only subarray with sum = 15 is [-5, 8, -14, 2, 4] of length 5.

Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].'''
class Solution:
    def longestSubarray(self, arr, k):
        # code here
        subarray={}
        sum,l=0,0
        for i in range(len(arr)):
            sum+=arr[i]
            if sum==k:
                l=i+1
            if sum-k in subarray:
                l=max(l,i-subarray[sum-k])
            if sum not in subarray:
                subarray[sum]=i
        return l


s=Solution()
long=s.longestSubarray([6,-15,-64 ,11 ,-45 ,22 ,-73 ,-2 ,71 ,7 ,6, -15 ,-64, 11, -45, 22 ,-73 ,-2 ,71, 7],-14)
print(long)