#quick_sort
def quick_sort(arr,low,high):
    if low<high:
        p=partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)
def partition(arr,low,high):
    p=high
    l=low
    r=high
    while(l<r):
        if arr[l]<arr[p]:
            l+=1
        elif arr[r]>=arr[p]:
            r-=1
        else:
            arr[l],arr[r]=arr[r],arr[l]
    arr[l],arr[p]=arr[p],arr[l]
    return l
arr=[10,23,4,57,24,84,2]
quick_sort(arr,0,6)
print(arr)