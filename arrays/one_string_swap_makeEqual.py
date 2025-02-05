'''You are given two strings s1 and s2 of equal length.
A string swap is an operation where you choose two indices in a string
(not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.



Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

 '''
class Solution:
    def swap(self,s1,s2,idx):
        if len(idx) == 2:
            if s1[idx[0]] == s2[idx[1]] and s1[idx[1]] == s2[idx[0]]:
                return True
            else:
                return False
        else:
            return False
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        l=len(s1)
        if s1 == s2:
            return True
        i=0
        idx=[]
        for k in s1:
            if i<l:
                if k == s2[i]:
                    pass
                else:
                    idx.append(i)
                i+=1
        return self.swap(s1,s2,idx)
if __name__ == "__main__":
    s=Solution()
    print(s.areAlmostEqual("npv","zpn"))
