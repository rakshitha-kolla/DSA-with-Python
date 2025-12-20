def merge_sort(arr,l,h):
    if l<h:
        mid=(l+h)//2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,h)
        merge(arr,l,mid,h)
def merge(arr,l,m,h):
    left=l
    right=m+1
    temp=[]
    while(left<=m and right<=h):
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        if arr[right]<arr[left]:
            temp.append(arr[right])
            right+=1
    while(left<=m):
        temp.append(arr[left])
        left+=1
    while(right <= h):
        temp.append(arr[right])
        right+=1
    for i in range(l,h+1):
        arr[i]=temp[i-l]
arr=[10,23,4,57,24,84,2]
merge_sort(arr,0,6)
print(arr)