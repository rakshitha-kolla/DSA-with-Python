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


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        elif s==goal:
            return True
        double_string=s+s
        return double_string.find(goal) != -1
