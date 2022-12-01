def number_invertedTriangle(length):
    for i in range(0,length):
        for j in range(length,i,-1):
            print(j,end=" ")
        print()

length=int(input())        
number_invertedTriangle(length)
