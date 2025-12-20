def sort(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

arr=[10,23,4,57,24,84,2]
sort(arr)
print(arr)