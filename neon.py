n=int(input("enter any number"))
squ=n*n
s=0
while squ>0:
    r=squ%10
    s=s+r
    squ=squ//10
    if(n==s):
        print("This is number neon")
else:
    print("Not neon number")


