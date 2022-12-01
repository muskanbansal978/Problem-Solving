def number_triangle(length):
    for i in range(1,length+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

length=int(input())        
number_triangle(length)
