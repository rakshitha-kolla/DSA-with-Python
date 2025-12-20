#bubble sort
def sort(arr):
    n=len(arr)
    for i in range(len(arr)):
        flag=0
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=1
        if not flag:
            break
arr=[10,23,4,57,24,84,2]
sort(arr)
print(arr)