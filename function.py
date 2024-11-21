#POSITIONAL ARGUMENT OF FUNCTION
'''def add (x,y,z):
    z=x+y+z
    print(z)
    #return z
p=int(input("enter 1st value"))
q=int(input("enter 2nd value"))
r=int(input("enter 3rd value"))
x=add(p,q,r)# (y=r,x=p,z=q) this KEYWORD ARGUMENT 
print(x)
'''
#KEYWORD ARGUMENT OF FUNCTION
# def add(*n):
#     print(n)
# 	sum=0
# 	for i in n:
# 	    sum = sum+i
# 	return sum
# var=add(10,20,30,40,50,60)
# print(var)


'''def add(*n):
    print(n)
    sum=0
    for i in n:
        sum = sum+i
    return sum
var=add(10,20,30,40,50,60)
print(var)'''
#-----------------------------------------------------------------------------
#KEYWORD VARIABLE-LENGTH ARGUMENT OF FUNCTION (** KWargs)
'''def show(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,"=",value)
show(name='pragati',age=24,qualification='B.Tech')'''
#-----------------------------------------------------------------------------

