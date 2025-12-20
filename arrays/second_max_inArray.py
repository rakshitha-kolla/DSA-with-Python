
def second_max(arr):
    maxi=-float('inf')
    s=-float('inf')
    for ele in arr:
        if ele >= maxi:
            s=maxi
            maxi=ele
        if ele > s and ele < maxi:
            s=ele
    return (maxi,s)
arr=[12,34,66,23,6,23,23,66]
print(second_max(arr))