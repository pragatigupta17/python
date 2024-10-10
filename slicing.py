#       0  1  2    3      4  5 6     7      8  9 10
lis1 = [12,3,44,'sourabh',56,7,88,'aditiya',33,4,5]
#     -11 -10 -9  -8      -9 -8 -7   -6    -5 -4 -3
print(lis1)
# lis [start:end:jump]
#jump --> default 1
#end --> excluded (just before end)
a=lis1[2:4:-1]
print(a)
b=lis1[3:8:1]
print(b)