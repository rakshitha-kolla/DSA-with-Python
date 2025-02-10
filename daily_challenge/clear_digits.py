'''You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

    Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.
Example 1:

Input: s = "abc"

Output: "abc"

Explanation:

There is no digit in the string.

Example 2:

Input: s = "cb34"

Output: ""

Explanation:

First, we apply the operation on s[2], and s becomes "c4".

Then we apply the operation on s[1], and s becomes "".

'''
class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for c in s:
            if c.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
if __name__=="__main__":
    s=Solution()
    print(s.clearDigits('c2b4d'))