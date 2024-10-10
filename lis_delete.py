# INPLACE FUNCTION --> are the functions in which no extra object has been created 
# its two type -->  1) sort , 2)inplace
lis1 = ['ajay','sourabh','aditya']
print(lis1)
lis1.reverse() #inpalce()
print(lis1)

"""  delete  element by using these four type """                                #NON RETURN FUN   |  RETURN FUN
# 1) POP                                                                            """ append()   |    Count() 
# 2)REMOVE                                                                               extend()  |    index()
# 3)CLEAR                                                                                 sort()   |    len()
# 4)DEL STATEMENT                                                                         reverse()|    max()
 #                                                                                         insert()|    min()
 #                                                                                                 |    sum()
# POP() ----> delete last element and also return deleted element                                  |    pop()
lis2 = ['ajay','sourabh','aditya','mandeep','aditiya']                        #                    |  return()
"""deleted_value = lis2.pop()                                                                      |  clear()
print(lis2)                                                                                        | remove()
print(deleted_value)                                                                               | del statement
deleted_value = lis2.pop(1)
print(lis2)"""
# --------------------------REMOVE
"""c=lis2.count('aditiya')
print(lis2)
lis2.remove('aditya')
print(lis2)"""
# ----------------------------CLEAR
"""print(lis2)
lis2.clear()
print(lis2)"""
# --------------------------DEL STATEMENT
print(lis2)
del lis2
print(lis2)