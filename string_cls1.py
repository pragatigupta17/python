# STRING CLASS 1 --> ITS IS IMMUTABLE
# LIST, SET, DICTONRY  THESE ARE MUTABLE
""" string : 1) sequence (ordered)
             2) immutable """
msg = "string is a immutable data-type"
print(msg[12:21])
# msg[3]="y"

# CAPAITALIZED() --> return capaitaized string
a= "my is pragati"
c = a.capitalize()
print(c)
#UPPER () -->
b=a.upper()
print(b) 
# LOWER ()-->
c=a.lower()
print(c)
# ISUPPER()--> RETURN BOOLEAN OUTPUT
d=a.isupper()
print(d)
data = "APPLE IS GOOD"
d=data.isupper()
print(d)
# ISLOWER
data2="apple is good"
g=data2.islower()
print(g)
data3 ="3455AD"
h=data3.islower()
print(h)
# ISALPHA()
msg="aAaBBa"
j=msg.isalpha()
print(j)
# ISDIGIT
msg2 ="09097897865"
k=msg2.isdigit()
print(k)