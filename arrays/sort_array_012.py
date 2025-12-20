'''
def sort_array(arr):
    hash={}
    for ele in arr:
        if ele==0:
            hash[0]=hash.get(0,0)+1
        elif ele==1:
            hash[1]=hash.get(1,0)+1
        else:
            hash[2]=hash.get(2,0)+1
    i=0
    while(hash[0]):
        arr[i]=0
        hash[0]-=1
        i+=1
    while(hash[1]):
        arr[i]=1
        hash[1]-=1
        i+=1
    while(hash[2]):
        arr[i]=2
        hash[2]-=1
        i+=1
    return arr'''
def sort_array(arr):
    low,mid,high=0,0,len(arr)-1
    while(mid<=high):
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
arr=[2,0,2,1,1,0]
print(sort_array(arr))
print(arr)