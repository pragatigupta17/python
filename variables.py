''' Variables and Data-type in Python'''
#-----------------------------------------#
'''VARIABLE or REFRENCE ---> variable is a refrence to a memory localtion where our object (data) resides.'''

num1 = 90                   # code        |   stack refrence  | Heap(object)
num2 = 100                           
num3 = 90                   #Instruction  |    num1,num2      |  90,100,90/  object value
print(id(num1))
print(id(num2))
print(id(num3))

