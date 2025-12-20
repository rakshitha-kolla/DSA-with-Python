def Binary_Search(arr,ele):
    l=0
    h=len(arr)
    while(l<h):
        mid=(l+h)//2
        if arr[mid]==ele:
            return mid
        elif arr[mid]>ele:
            h=mid-1
        else:
            l=mid+1
    return -1
print(Binary_Search([2,3,4,5,6,7,8],8))
print(Binary_Search([2,3,4,5,6,7,8],10))