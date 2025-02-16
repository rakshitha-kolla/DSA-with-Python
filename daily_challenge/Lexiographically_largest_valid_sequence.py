from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        length = 2 * n - 1  # Length of the sequence
        sequence = [0] * length  # Initialize the sequence with zeros
        used = [False] * (n + 1)  # Track which numbers have been used

        def backtrack(index):
            # Base case: If all positions are filled, return the sequence
            if index == length:
                return True

            # If the current position is already filled, move to the next position
            if sequence[index] != 0:
                return backtrack(index + 1)

            # Try placing the largest possible number first (to ensure lexicographical order)
            for num in range(n, 0, -1):
                if not used[num]:
                    # Handle the number 1 separately (it appears only once)
                    if num == 1:
                        sequence[index] = 1
                        used[1] = True
                        if backtrack(index + 1):
                            return True
                        # Backtrack
                        sequence[index] = 0
                        used[1] = False
                    else:
                        # For numbers > 1, ensure the second occurrence is at the correct distance
                        if index + num < length and sequence[index + num] == 0:
                            sequence[index] = num
                            sequence[index + num] = num
                            used[num] = True
                            if backtrack(index + 1):
                                return True
                            # Backtrack
                            sequence[index] = 0
                            sequence[index + num] = 0
                            used[num] = False
            return False

        backtrack(0)
        return sequence

s=Solution()
print(s.constructDistancedSequence(5))