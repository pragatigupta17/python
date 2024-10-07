'''SEQUENCE ----> ORDER DATA-TYPE '''
# to maintain at sequence data-type we use indexing...

""" LIST ---> LIST """
#list in python when be to store multiply element with the help of single refrence (variable) then we have two option .
""" 1) list
2) tuple """
# list is a container in which be contain Hitroginous data as well as homogenous data.
# NOTE ----> Array is not a buliding sport in python.

# Represtation of list :- [] 

""" ------------------------------"""

#forwordindexing   0  , 1 ,  2
""" st_detail = [name,age,address]"""
#backwordindexing  -3 ,  -2 , -1


name = "pragati"
age = 24
address = "bhopal"
st_detail_1 = [name,age,address] #list
st_detail_2 = ["ajay",34,"ujjain"]
print(type(name))
print(type(age))
print(type(address))
print(type(st_detail_1))
print(st_detail_1[0],st_detail_1[-3])
print(st_detail_1[-1])
print(st_detail_1[-2])

 # LIST MANIPULATE:---> list is a mutable datatype, it means u can change data information as u want 
st_detail_2[2]="indore"
print(st_detail_2)
st_detail_2[-3]="vijay"
print(st_detail_2)

#EMPTY LIST
# 1)
lis=[]
# 2) LIST METHOD
li = list()
print(lis)
print(li)
#ANY()

print(any(lis)) #false  if its filled with data it return true otherwise return false
lis=[56]
print(any(lis)) #true 