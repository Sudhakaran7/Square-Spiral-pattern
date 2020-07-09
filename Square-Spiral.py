num=int(input())
arr=[[0 for i in range(num)] for y in range(num)]
n=1
low=0
high=num-1
flag=int((num+1)/2)
for i in range(flag):
  for j in range(low,high+1):
    arr[i][j]=n
    n=n+1
  for j in range(low+1,high+1):
    arr[j][high]=n
    n=n+1
  for j in range(high-1,low-1,-1):
    arr[high][j]=n
    n=n+1
  for j in range(high-1,low,-1):
    arr[j][low]=n
    n=n+1
  low+=1
  high-=1
for i in range(num):
  for j in range(num):
    print(arr[i][j],end='\t')
  print()
