def binary_search(arr,val,lower,upper):
    if upper >= lower:
        mid=(lower+upper)//2
        if arr[mid]== val:
            return mid
        elif arr[mid]> val:
            return binary_search(arr,val,lower,mid-1)
        else:
            return binary_search(arr,val,mid+1,upper)
    else:
        return -1
        
    
if __name__=="__main__":
    arr=[]
    n=int(input("Enter size of array "))
    for i in range(n):
        element=int(input("Enter the element of array "))
        arr.append(element)
    val=int(input("Enter value to be searched "))
    lower=0
    upper=len(arr)-1
    print("Element",val,"found at index",binary_search(sorted(arr),val,lower,upper))

