
# sum of odd prime numbers less than or equal to n
class Solution:
	def prime_Sum(self, n):
		prime = [True] * (n + 1)
		prime[0] = prime[1] = False
		for i in range(2, int(n ** 0.5) + 1):
			if prime[i]:
				for j in range(i * i, n + 1, i):
					prime[j] = False
		sum_ = 0
		for i in range(len(prime)):
			if prime[i] and i % 2 != 0:
				sum_ += i
		return sum_
s = Solution()
n = int(input())
print(s.prime_Sum(n))
	