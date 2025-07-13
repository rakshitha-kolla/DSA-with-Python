class Solution:
    def matchPlayersAndTrainers(
        self, players: list[int], trainers: list[int]
    ) -> int:
        players.sort()
        trainers.sort()
        m, n = len(players), len(trainers)
        i = j = count = 0

        while i < m and j < n:
            while j < n and players[i] > trainers[j]:
                j += 1
            if j < n:
                count += 1
            i += 1
            j += 1

        return count
s=Solution()
print(s.matchPlayersAndTrainers( [1,1,1],  [10]))