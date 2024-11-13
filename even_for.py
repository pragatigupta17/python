n=int(input("enter any no:"))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
    if i<=(n-2):
        print(i,end='+')
    else:
        print(i,end='=')
print(sum)
