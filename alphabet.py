n=input("enter an string:")
v=0
c=0
for i in n:
    x=['a','e','i','o','u','A','E','I','O','U']
    if i in x:
        v=v+1
    else:
        c=c+1
print(v)
print(c)
    