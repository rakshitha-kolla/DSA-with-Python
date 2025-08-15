class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n%4==0:
            n=n//4
        return n==1
s=Solution()
print(s.isPowerOfFour(16))  # True
print(s.isPowerOfFour(5))   # False
print(s.isPowerOfFour(1))   # True
print(s.isPowerOfFour(0))   # False
print(s.isPowerOfFour(-4))  # False
print(s.isPowerOfFour(64))