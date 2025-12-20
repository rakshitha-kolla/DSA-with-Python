# insertion sort
def sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        key=arr[i]
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
arr=[10,23,4,57,24,84,2]
sort(arr)
print(arr)