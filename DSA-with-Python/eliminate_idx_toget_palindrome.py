def is_palindorme(s,left,right):
    while(left<=right):
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            return False
    return True
def get_idx(s):
    n=len(s)
    left=0
    right=n-1
    while(left <= right):
        if s[left]==s[right]:
            pass
        else:
            if is_palindorme(s,left+1,right):
                return left
            if is_palindorme(s,left,right-1):
                return right
        left+=1
        right-=1
    return -1
s=input("Enter string: ")
print(get_idx(s))