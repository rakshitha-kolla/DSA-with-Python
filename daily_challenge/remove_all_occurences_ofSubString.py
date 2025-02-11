'''class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
      l=list(s)
      pl=len(part)
      while(True):
        if part in s:
            i=s.find(part)
            del l[i:i+pl]
            s="".join(l)
        else:
            return s'''
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s=s.replace(part,"",1)
        return s
if __name__=="__main__":
    s=Solution()
    si=s.removeOccurrences("wwwwwwwwwwwwwwwwwwwwwvwwwwswxwwwwsdwxweeohapwwzwuwajrnogb",'w')
    print(si)