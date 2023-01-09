def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i,0,-1):
            if arr[j-1]>arr[j] and j>0:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j=j-1
    return arr

arr=[1,3,2,4,1,0]
print(insertion_sort(arr))
