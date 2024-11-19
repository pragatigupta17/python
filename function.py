#POSITIONAL ARGUMENT OF FUNCTION
def add (x,y,z):
    z=x+y+z
    print(z)
    #return z
p=int(input("enter 1st value"))
q=int(input("enter 2nd value"))
r=int(input("enter 3rd value"))
x=add(p,q,r)# (y=r,x=p,z=q) this KEYWORD ARGUMENT 
print(x)
