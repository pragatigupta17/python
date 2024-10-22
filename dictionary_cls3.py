#METHOD OF DICT ---->
# ZIP method -->
key=["ajay","vikas","arun","sonam","naman"]
value=[23,23,45,24,26]
result = dict(zip(key,value))
print(result)
ans=tuple(zip(key,value))
print(ans) 
lis=list(zip(key,value))
print(lis)
 
# GET(key) --> return value
data = {"ajay":23,"vikas":54,"mohan":21} 
a=data['mohan']
print(a)
b=data.get('ajay')
print(b)

# SETDEFAULT()
# 1) key available --> return existing value.
# 2) key not available --> 1) key-value pair add,
#                         2) return added value.
data1={'1':2345,'2':7890,'3':45667}
print(data1)
value = data1.setdefault('11',4567)
print(value)

# POP(), POPITEM() ---> return value 
# CLEAR() -->remove value

data2={'1':2345,'2':7890,'3':45667}
print(data2)
value2 = data2.pop('2')
print(value2)
print(data2)
data3={'1':2345,'2':7890,'3':45667}
print(data3)
value3 = data3.popitem() # deleted last value key pair
print(value3)
print(data3)
num={'1':2390,'2':2378,'3':45667,
'4':{'11':4567,'22':45678,'44':34567}}
print(num)
num1=num.pop(['4'][34567])
print(num1)


