'''Given two positive integers left and right, find the two integers num1 and num2 such that:

    left <= num1 < num2 <= right .
    Both num1 and num2 are

    .
    num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.

Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].



Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
'''
class Solution:
    def _sieve(self,upper_limit):
        sieve=[True]*(upper_limit+1)
        sieve[0]=sieve[1]=False
        for num in range(2, int(upper_limit*0.5) +1):
            if sieve[num]:
                for i in range(num*num,upper_limit+1,num):
                    sieve[i]=False
        return sieve
    def closestPrimes(self, left: int, right: int) -> list[int]:
        sieve_arr=self._sieve(right)
        prime_num = [ num for num in range(left,right+1) if sieve_arr[num] ]
        if len(prime_num)<2:
            return [-1,-1]
        diff=9999999999
        idx=-1
        for i in range(1,len(prime_num)):
            if prime_num[i]-prime_num[i-1]<diff:
                diff=prime_num[i]-prime_num[i-1]
                idx=i
        return [prime_num[idx-1],prime_num[idx]]
s=Solution()
print(s.closestPrimes(10,19))