'''You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.



Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:

Input: tiles = "AAABBC"
Output: 188

Example 3:

Input: tiles = "V"
Output: 1
'''
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles=sorted(tiles)
        used=[False]*len(tiles)
        return self.backtrack(tiles,used)
    def backtrack(self,tiles,used):
        count=0
        for i in range(len(tiles)):
            if used[i] or (i>0 and tiles[i] == tiles[i-1] and not used[i-1]):
                continue
            used[i]=True
            count += 1 + self.backtrack(tiles, used)
            used[i]=False
        return count
s=Solution()
print(s.numTilePossibilities("AAB"))