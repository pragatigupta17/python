#cursor pattern |>
n=int (input("enter row no:"))
i=1
while i<n:
    print('*'*i+''*(n-1))
    i=i+1
i=i-2
while i>0:
    print('*'*i+''*(n-1)) #('*'*i)
    i=i-1
   