num=int(input("enter any number"))
main=num
sum=0
while num>0:
    r=num%10
    sum=sum+r
    num=num//10
if(main%sum==0):
    print(main,"Harshad number")
else:
    print(main,"Not harshad number")