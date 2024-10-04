#logical_operator
# 1) AND 
'''  Input1 | Input2 |   result
      0    | 0      |   0  
      0    | 1      |   1
      1    | 0      |   1
      1    | 1       |   1  '''

#----------------------------

# 2) OR
''' Input |  result
    0     |   1
    1     |   0 '''

# ----------------------

# 3) NOT

print(True and True)
print(3>2 and 34>5)
print(not(24>56))

# membership operator
# in , not in

string1 ="apple is good 4 health"
print("is" in string1) #True
print("si" in string1) #False
print("apple is" in string1) #False bcz after is no space 
print("4" in strin1) #True
print("health" not in string1) #False

# Identity Operator
# is , is not
''' is operator give True when test for same object otherwise False.'''

