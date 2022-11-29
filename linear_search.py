def linear_search(arr,target):
  ans=-1
  for idx,val in enumerate(arr):
    if val==target:
      ans=idx
      break
  return ans

length=int(input())
arr=[]
for i in range(0,length):
  arr.append(int(input()))
target=int(input())
print(linear_search(arr,target))
