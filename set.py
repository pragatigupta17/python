# SET --> datatype
""" 1) set  is a collection of data 
    2) set is a container in which we contain multiple data, but duplication is not allowed,
        and it is an unordered datatype.
    3) where our main concern is data , but not any order related to it , then we use set. 
    4) there are three types of set 1)INTERSECTION, 2)UNION, 3)SET_DIFFERENCE """
A={1,3,9,9,7,2,5}
B={2,3,99,11,5}
# A intersection B {3,2,5} it represent with (&)
# A union B {1,7,9,3,2,5,99,11} it represent with (|)
# A set_difference B it represent with (-) 
"""A-B={1,7,9}
B-A={99,11}"""
s1={1,2,3,3,4,9,11,17}
s2={4,5,9,17,89}
s3={"a","b",1,2,3,88}
print(s1)
r=s1. union(s2,s3)
#r=s1|s2|s3
print(r)
i=s1 .intersection(s2,s3)
#i=s1&s2&s3
print(i)
s=s1. difference(s2,s3)
print(s)
j=s2. difference(s1)
print(j)
l=s1. difference(s2,s3)
print(l)
a={'a','a','b','f','y','t'}
b={'b','y','1','6','7'}
c={99}
d=a. difference(b)
f=a. difference(c)
print(d)
print(f)
a.update(b)
print(a)
a.add(786)
print(a)
b.add(5678)
print(b)
c.update(b)
print(c)
c.add(1119)
print(c)