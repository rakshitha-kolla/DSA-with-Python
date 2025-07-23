class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_score=0
        hpriority="ab" if x>y else "ba"
        lpriority="ba" if hpriority == "ab" else "ab"
        string_after_first_pass=self.remove_substring(s,hpriority)
        removed_pairs_count=(len(s)-len(string_after_first_pass))//2
        total_score+=max(x,y)*removed_pairs_count
        string_after_second_pass=self.remove_substring(string_after_first_pass,lpriority)
        removed_pairs_count=(len(string_after_first_pass)-len(string_after_second_pass))//2
        total_score+=min(x,y)*removed_pairs_count
        return total_score
    def remove_substring(self,s,tp):
        stack=[]
        for char in s:
            if (char==tp[1] and stack and stack[-1]==tp[0]) :
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
s=Solution()
print(s.maximumGain("cdbcbbaaabab", x = 4, y = 5))