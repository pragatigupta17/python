d={1:"mon",2:"tue",3:"wed"}
d.update({4:"thus"})
d[5]="fri"
print(d)
# list as a value in dictionary,
# dictionary as a value in dictionary
d={1:["ajay",23,"bhopal"],2:["aditya",24,"ujjain"]}
print(d)
print(d[1])
print(d[1][2])
d[2][2]="indore"
print(d)
# d.update({2:["aditya",24,"ujjain"]})
d1 = {101:{"name":"ajay","age":23,"city":"bhopal"},
      102:{"name":"jay","age":23,"city":"ujjain"}}
print(d1)
print(d1[101])
print(d1[101]["city"])
d1[102]["city"]="indore"
print(d1)
#use of update
d1[102].update({"city":"ratlam"})
print(d1)

#method of dictionary
d= {1:"mon",-2:"tue",3:"wed"}
#KEYs
keys=d.keys()
print(keys,type(keys))
#VALUEs
values=d.values()
print(values,type(values))
#ITEMs
items=d.items()
print(items,type(items))

sorted_keys=sorted(d.keys())
print(keys,type(keys))

