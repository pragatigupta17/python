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