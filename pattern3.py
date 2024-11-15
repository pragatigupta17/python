#opposit arrow
n=int(input("enter row no:"))
i=1
while i<=n:
    print(' '*(n-i)+'*'*i)
    i=i+1
i=i-2
while i>0:
    print((n-i)*' '+'*'*i)
    i=i-1