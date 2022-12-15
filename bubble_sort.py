def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
    return arr

if __name__=="__main__":
    size=int(input("Enter the size of array "))
    arr=[]
    for i in range(size):
        element=int(input("Enter the element "))
        arr.append(element)
    print(bubble_sort(arr))
