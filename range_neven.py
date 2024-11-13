n=int(input("enter any no:"))
sum=0
for i in range(1,n+1):
    sum=sum+2*i
    if i<=(n-1):
        print(2*i,end='+')
    else:
        print(2*i,end='=')
print(sum)
