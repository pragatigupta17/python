# REPLACE(old_value,new_value)
s="we are her to learn c++ , it is a high level language"
s1=s.replace("c++","python")
print(s1)
s2=s.replace('a','b')
print(s2)
s3=s.replace('l','m',2)
print(s3)
s4=s.replace(s,"new")
print(s4)

#SPLIT() --> return list 
r="we are her to learn c++ , it is a high level language"
r1= r.split()
print(r1)
r2=r.split('a')
print(r2)

#JOIN() --->return string
j=["apple","banana","pineapple","mango"]
k=["kjkj","xgfh"]
j1="".join(j)
print(j1)
j2=",".join(j)
print(j2)
j3=" ".join(j) +"  "+" ".join(k)
print(j3)
#slice,join,split
s="its now or never"
#"sti.won.ro.reven"
s= s.split()
print(r1) #['its', 'now', 'or', 'never']
a=s[0][::-1]
b=s[1][::-1]
c=s[2][::-1]
d=s[3][::-1]
s=[a,b,c,d]
print(s)


