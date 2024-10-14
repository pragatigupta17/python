# slicing is used to get slice (subsequence) of a sequence 
#      0  1  2    3      4  5 6     7      8  9 10
lis1 = [12,3,44,'sourabh',56,7,88,'aditiya',33,4,5]
#     -11 -10 -9  -8      -9 -8 -7   -6    -5 -4 -3
print(lis1)
a=lis1[3:]
print(a)
a=lis1[3::2]
print(a)
a=lis1[3:7]+lis1[8:]
print(a)
a=lis1[7:2:-1]
print(a)
a=lis1[-4:-9:-1]
print(a)
a=lis1[::-1]
print(a)

# string----->

st="we are here to learn python . and slicing is very helpful"
b=st[:20]
print(b)
c=st[34:]
print(c)
print(st[3:19:3])
print(st[:21]+"cpp"+st[27:])
