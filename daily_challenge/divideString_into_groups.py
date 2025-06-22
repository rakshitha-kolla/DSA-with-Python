class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        res = []  # grouped string
        n = len(s)
        curr = 0  # starting index of each group
        # split string
        while curr < n:
            res.append(s[curr : curr + k])
            curr += k
        # try to fill in the last group
        res[-1] += fill * (k - len(res[-1]))
        return res
s=Solution()
print(s.divideString( "abcdefghi",  3, "x"))