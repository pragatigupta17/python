'''n=int(input("enter any no:"))
i=1
while i<=n:
    if i%2!=0:
      print(i,end=' ')
    i=i+1'''
n=int(input("enter any no:"))
i=1
sum=0
while i<=n:
  if i%2!=0:
    sum=sum+i
    if i<=(n-2):
        print(i,end='+')
    else :
        print(i,end='=')
  i=i+1
print(sum)

    