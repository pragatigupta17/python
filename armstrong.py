n = int(input("Enter a number: "))
store =n
s=0
while n>0:
    r=(n%10)
    s=s+r*r*r
    n=n//10
if(store==s):
    print("this is Armstrong")
else:
    print("this is not Armstrong")
    

