def linear_serach(arr,ele):
    for i in range(len(arr)):
        if arr[i]==ele:
            return i
    return -1
print(linear_serach([3,10,35,63,23],3))