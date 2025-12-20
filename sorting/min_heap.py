
def heapify(arr,n,i):
    smallest=i
    left=2*i+1
    right=left+1
    if left<n and arr[left]<arr[smallest]:
        smallest=left
    if right<n and arr[right]<arr[smallest]:
        smallest=right
    if i!=smallest:
        arr[smallest],arr[i]=arr[i],arr[smallest]
        heapify(arr,n,smallest)
def buid_min_heap(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
def min_heap_sort(arr):
    buid_min_heap(arr)
    sorted_arr=[]
    n=len(arr)
    for i in range(n):
        arr[0],arr[n-i-1]=arr[n-i-1],arr[0]
        sorted_arr.append(arr[n-i-1])
        heapify(arr,n-i-1,0)
    return sorted_arr
arr=[10,23,4,57,24,84,2]
print(min_heap_sort(arr))