""" TUPLE --> 1) it is sequence data type(order datatype).
              2) it is immutable data type.
              3) a) Representation (),
                 b) comma seperated
              4) it is faster than list , memory efficient.
              5) single element representation.
              6) generally whenever data is fetched from database it is stored in the form of tuple or dictionary.
              7) it is a container which store multiply data (hetrogenous)."""
lis =[2,3,4]
lis[1]=90                                               # STACK(REFERENCE VARIABLE)   |  HEAP(OBJECT)
print(lis)                                              #         APPLE               |  string-"apple"=736
fruit = ("apple",20,100)                                #                             |address of string 
print(type(fruit))                                      #                             | 20=080 address string
print(id(fruit[0]),id(fruit[1]),id(fruit[2]))           #                             |
fruit = ("apple",20,100) + ("banana",999)               #                             | 100 = 640 address string
fruit = ("apple",20,100,"banana",999)                   #                             | ---------------------------
fruit = 99999999999999                                  #                             | | 736 |   080  |  690 |
print(fruit)                                            #                             |  656 = address of tuple
"""NOTE -->    """         
number= (12,99) + (78,90) #2 tuple
number=number + (89,90)# 2 tuple
print(number) # 1 tuple (12,99,78,90,89,90) there are total 5 tuples in this number list
#             0            1
lis = [["ajay","aman"],(45,67)] 
#          0     1       0  1
#print(type(lis[1]))
#lis[1][0]=99
lis.pop()
print(lis)
t=(34,55,[3,4,555])  
print(t)
t[2][1]=99999
print(t)
t[2].append(88888)
print(t)
lis2 = [["ajay","aman"],(45,[67,44])]
print(type(lis2))
#lis2[1]=999
#lis2[0]=888
print(lis2)
print(type(lis2[1]))
lis2[1][1][1]=88
print(lis2)

         