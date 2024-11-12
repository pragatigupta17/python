# EVEN NO 1 - 10 AND ALSO SUM OF THESE NO 
# 2 4 6 8 10 = sum 
n=int(input("enter any no:"))
i=1
sum=0
while i<=n:
  if i%2==0:
    sum=sum+i
    if i<=(n-2):
        print(i,end='+')
    else :
        print(i,end='=')
  i=i+1
print(sum)
'''else:
    if i%2==0:
      if i<=(n-2):
        print(i,end=',')
      else:
        print(i)'''



    