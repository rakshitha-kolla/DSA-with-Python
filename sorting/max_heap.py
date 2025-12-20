
def heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=left+1
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if i != largest:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n,largest)
def buid_max_heap(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
def max_heap_sort(arr):
    n=len(arr)
    buid_max_heap(arr)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
    return arr
arr=[10,23,4,57,24,84,2]
print(max_heap_sort(arr))