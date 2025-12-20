#reverse an array in place

def reverse_array(arr):
    for i in range(len(arr)//2):
        arr[i],arr[-(i+1)]=arr[-(i+1)],arr[i]
    return arr
print(reverse_array([1,2,3,4,5]))