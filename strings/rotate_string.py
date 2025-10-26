class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        elif s==goal:
            return True
        n=len(s)
        for i in range(n):
            if s[i+1:]+s[:i+1] == goal:
                return True
        return False
s=Solution()
print(s.rotateString("abcde","cdeab"))  # True  