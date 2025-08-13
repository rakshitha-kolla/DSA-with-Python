class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 :
            return False
        while n %3 == 0:
            n //= 3
        return n == 1
s=Solution()
print(s.isPowerOfThree(27))  # Example usage, should return True
print(s.isPowerOfThree(10))  # Example usage, should return False   