n=int(input("enter any no:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    if i<=(n-1):
        print(i*2-1,end='+')
    else:
        print(i*2-1,end='=')
print(sum)
