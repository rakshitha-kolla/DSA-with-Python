class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        res = []
        n = len(words)
        for i in range(n):
            if x in words[i]:
                res.append(i)
        return res
s=Solution()
print(s.findWordsContaining( ["leet","code"], "e"))